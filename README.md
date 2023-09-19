# skynet-dev

Stochastic parrot experiments.

See if you can beat a stochastic parrot at Chess @ https://ParrotChess.com/ :D
Powered by GPT-3.5. It uses the same basic prompting technique and the same
OpenAI model (gpt-3.5-turbo-instruct) as checkmate.py in this repo, but it
lets you play interactively against GPT-3.5 in the browser instead of GPT-3.5
playing against Stockfish.

## Install Python dependencies

```pip install openai chess stockfish```

## Install Stockfish

On Debian/APT-based Linux distributions:
```apt install stockfish```

On macOS with Homebrew:
```brew install stockfish```

## Run Chess experiment

```
export OPENAI_KEY=<your-openai-API-key>
./checkmate.py
```

![GPT-3.5 vs Stockfish 1700 ELO](checkmate.gif)

