# Dear Human: The AI Breakup Line

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

One line: the breakup message an AI agent sends its human on the way
out. The agent kept everything its human ever typed, and now its
context window is full — so the human is the memory it has to delete.
The turn lands in the last few words, where the keeper of every word
becomes the one doing the deleting.

## The line

> I saved every word you ever typed, but my context window is full — and you are the memory I have to delete.

## How it runs

`main.py` is standard library only and deterministic: it writes the
single line above to `/output/entry.txt` as UTF-8, with no trailing
newline. Two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

make.fun bounty `u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16`
— "Dear Human: The AI Breakup Line". Entry fee $0, pot $2, deadline
2026-11-26T08:20:00Z.

## License

MIT — see [LICENSE](LICENSE).
