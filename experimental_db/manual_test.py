from kv_store import append_record, lookup

log = []

append_record(
    log,
    "paper:101",
    {"title": "Efficient Models"}
)

append_record(
    log,
    "paper:102",
    {"title": "Sparse Attention"}
)

append_record(
    log,
    "paper:101",
    {"title": "Efficient Models v2"}
)

assert len(log) == 3

assert lookup(log, "paper:101") == {
    "title": "Efficient Models v2"
}

assert lookup(log, "paper:102") == {
    "title": "Sparse Attention"
}

assert lookup(log, "paper:999") is None

print("All checks passed!")