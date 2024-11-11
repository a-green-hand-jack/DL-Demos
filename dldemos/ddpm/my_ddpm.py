import torch


class MyDDPM:
    # 因为DDPM仅仅是维护了前向和反向过程中的一些计算过程，本身不涉及到可学习的神经网络参数，所以不用继承nn.Module

    def __init__(
        self, device, n_steps: int, min_beta: float = 0.0001, max_beta: float = 0.02
    ) -> None:
        betas = torch.linspace(min_beta, max_beta, n_steps).to(device)
        # \alpha_t = 1 - \beta_t
        alphas = 1 - betas
        # \bar{\alpha}_t = \prod_{i=1}^t \alpha_{i}
        alpha_bars = torch.empty_like(alphas)  # 提前分配显存，速度快些
        product = 1
        for i, alpha in enumerate(alphas):
            product *= alpha
            alpha_bars[i] = product

        self.betas = betas
        self.n_steps = n_steps
        self.alphas = alphas
        self.alpha_bars = alpha_bars

        self.device = device

    def sample_forward(
        self, x: torch.Tensor, t: torch.Tensor, eps=None
    ) -> torch.Tensor:
        """
        x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} eps
        """
        if eps is None:
            eps = torch.randn_like(x)

        alpha_bar_t = torch.gather(self.alpha_bars, 0, t)  # 第0个维度是batch size
        x_t = torch.sqrt(alpha_bar_t) * x + torch.sqrt(1 - alpha_bar_t) * eps

        return x_t

    def sample_backward(
        self,
        img_shape,
        net,
        simple_var=True,
    ) -> torch.Tensor:
        x = torch.randn(img_shape).to(self.device)
        net = net.to(self.device)

        for t in reversed(range(self.n_steps)):
            x = self.sample_backward_step(
                x,
                t,
                net,
                simple_var,
            )
        return x

    def sample_backward_step(
        self,
        x_t,
        t,
        net,
        simple_var=True,
    ) -> torch.Tensor:
        n = x_t.shape[0]
        t_tensor = torch.tensor([t] * n, dtype=torch.long).to(self.device).unsqueeze(1)

        eps = net(x_t, t_tensor)

        if t == 0:
            noise = 0
        else:
            if simple_var:
                var = self.betas[t]
            else:
                var = (
                    (1 - self.alpha_bars[t - 1])
                    / (1 - self.alpha_bars[t])
                    * self.betas[t]
                )

            noise = torch.randn_like(x_t)
            noise *= torch.sqrt(var)

        mean = (
            1
            / torch.sqrt(self.alphas[t])
            * (x_t - (1 - self.alphas[t]) / (1 - self.alpha_bars[t]) * eps)
        )
        x_t = mean + noise

        return x_t
