from fastapi import APIRouter, Depends
from models import Node, Music, MusicId
from typing import Annotated, List
from db import music_db
from linkedlist import playlist


music_router = APIRouter()


@music_router.get('/music-list')
def music_list(db: Annotated[List[Music], Depends(music_db)]):
    return db


@music_router.post('/add-to-playlist')
def add_to_playlist(body: MusicId, db: Annotated[List[Music], Depends(music_db)]):
    music_id: int = body.music_id
    music: Music = Music(**list(filter(lambda x: x["id"] == music_id, db))[0])
    node: Node = Node(music=music)
    return {
        'playlist': playlist.add_music(node),
        'current': playlist.current.music
    }


@music_router.post('/play-music')
def play_music(body: MusicId, db: Annotated[List[Music], Depends(music_db)]):
    playlist.play_music(body.music_id)
    return {
        'playlist': playlist.get_playlist(),
        'current': playlist.current.music
    }


@music_router.get('/current-music-playing')
def current_music_playing():
    return {
        'current': playlist.current.music
    }


@music_router.get('/play-next')
def play_next():
    playlist.play_next()
    return {
        'current': playlist.current.music
    }


@music_router.get('/play-previous')
def play_previous():
    playlist.play_previous()
    return {
        'current': playlist.current.music
    }


@music_router.get('/playlist')
def get_current_playlist():
    return playlist.get_playlist()