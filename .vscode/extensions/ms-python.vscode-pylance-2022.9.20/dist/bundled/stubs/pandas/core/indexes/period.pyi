import numpy as np
from pandas.core.indexes.datetimelike import (
    DatetimeIndexOpsMixin as DatetimeIndexOpsMixin,
)
from pandas.core.indexes.numeric import Int64Index

class PeriodIndex(DatetimeIndexOpsMixin, Int64Index):
    def __new__(
        cls,
        data=...,
        ordinal=...,
        freq=...,
        tz=...,
        dtype=...,
        copy: bool = ...,
        name=...,
        **fields,
    ): ...
    @property
    def values(self): ...
    def __contains__(self, key) -> bool: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __array_wrap__(self, result, context=...): ...
    def asof_locs(self, where, mask): ...
    def astype(self, dtype, copy: bool = ..., how: str = ...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    @property
    def is_full(self) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def get_value(self, series, key): ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def get_indexer_non_unique(self, target): ...
    def get_loc(self, key, method=..., tolerance=...): ...
    def insert(self, loc, item): ...
    def join(
        self,
        other,
        how: str = ...,
        level=...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    def intersection(self, other, sort: bool = ...): ...
    def difference(self, other, sort=...): ...
    def memory_usage(self, deep: bool = ...): ...

def period_range(
    start=..., end=..., periods=..., freq=..., name=...
) -> PeriodIndex: ...
