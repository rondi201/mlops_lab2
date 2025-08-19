from os import PathLike

from fedot.core.data.data import InputData
from fedot.core.data.data_split import train_test_data_setup


def load_fedot_train_data_from_csv(
    data_path: PathLike,
    task: str,
    target_columns: str | list[str | int],
    index_col: str | None = None,
) -> tuple[InputData, InputData]:
    """Загрузить данные для обучения и разбить их на train и test"""
    data = InputData.from_csv(
        data_path, task=task, index_col=index_col, target_columns=target_columns
    )
    return train_test_data_setup(data, shuffle=task != "ts", random_seed=42)  # type: ignore
