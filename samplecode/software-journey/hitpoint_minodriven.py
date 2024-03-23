class HitPoint:
    MIN: Final[int] = 0
    MAX: Final[int] = 999

    def __init__(self, value: int) -> None:
        if value < self.MIN:
            raise ValueError(f"{self.MIN}以上を指定してください")
        if value > self.MAX:
            raise ValueError(f"{self.MAX}以下を指定してください")

        self.value = value

    def damage(self, damage_amount: int) -> HitPoint:
        """ダメージを受ける"""

    def recover(self, recovery_amount: int) -> HitPoint:
        """回復する"""
