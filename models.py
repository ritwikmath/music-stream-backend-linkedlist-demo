from pydantic import BaseModel
from typing import Self

class Music(BaseModel):
    """Music class represent individual music object in songs.json"""
    id: int
    name: str


class Node(BaseModel):
    """Node used to implement DoublyLinkedList"""
    prev: Self | None = None
    music: Music
    next: Self | None = None


class MusicId(BaseModel):
    """Payload for add_to_playlist and play_music views"""
    music_id: int