import tekore as tk


def setup() -> tk.Spotify:
    client_id = "cb0b12f278584cbd8b2eb91ee23b116d"
    client_secret = "fba31d011fdd42e98bb28e98d4a92529"
    redirect_uri = "https://localhost"

    conf = (client_id, client_secret, redirect_uri)
    token = tk.prompt_for_user_token(*conf, tk.scope.every)

    spotify = tk.Spotify(token)
    return spotify


def bpm_for_current_track(spotify: tk.Spotify) -> float:
    current_track = spotify.playback_currently_playing()
    track_name = current_track.item.name
    track_artist = current_track.item.artists
    track_id = current_track.item.id
    print(f"{track_name=}, {track_artist=}")
    track_feat = spotify.track_audio_features(track_id)
    return track_feat.tempo


if __name__ == "__main__":
    spotify = setup()
    bpm = bpm_for_current_track(spotify)
    print(f"Current Track BPM is {bpm=}")
