#!/usr/bin/env python3

from stockfish import Stockfish

import openai
import chess
import os

openai.api_key = os.getenv('OPENAI_KEY')

stockfish = Stockfish()
stockfish.set_elo_rating(1700)
board = chess.Board()

pgn = """[Event "FIDE World Championship Match 2024"]
[Site "Los Angeles, USA"]
[Date "2024.12.01"]
[Round "5"]
[White "Carlsen, Magnus"]
[Black "Nepomniachtchi, Ian"]
[Result "1-0"]
[WhiteElo "2885"]
[WhiteTitle "GM"]
[WhiteFideId "1503014"]
[BlackElo "2812"]
[BlackTitle "GM"]
[BlackFideId "4168119"]
[TimeControl "40/7200:20/3600:900+30"]
[UTCDate "2024.11.27"]
[UTCTime "09:01:25"]
[Variant "Standard"]

1."""

n = 1
while True:
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=pgn,
        temperature=0,
        max_tokens=4,
    )

    san_move = response.choices[0].text.strip().split()[0]
    uci_move = board.push_san(san_move).uci()
    pgn += f" {san_move}"

    stockfish.make_moves_from_current_position([f"{uci_move}"])
    print("\033c" + stockfish.get_board_visual())

    if board.is_checkmate():
        print(pgn)
        print("GPT-3.5 won!")
        break

    if board.is_stalemate():
        print(pgn)
        print("Draw!")
        break

    uci_move = stockfish.get_best_move()
    move = chess.Move.from_uci(uci_move)
    san_move = board.san(move)
    board.push(move)
    pgn += f" {san_move}"

    stockfish.make_moves_from_current_position([f"{uci_move}"])
    print("\033c" + stockfish.get_board_visual())

    if board.is_checkmate():
        print(pgn)
        print("Stockfish 1700 ELO won!")
        break

    if board.is_stalemate():
        print(pgn)
        print("Draw!")
        break

    n += 1
    pgn += f" {n}."
