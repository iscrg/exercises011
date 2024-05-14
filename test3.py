from solution3 import Album, Track

albums = []
with open('Immersion_tracks.txt') as f:
    title, release_year, artist = f.readline().rstrip('\n').split('|')
    tracks = []
    for line in f.readlines():
        tTitle, tDuration, tArtist = line.rstrip('\n').split('|')

        if tArtist != '':
            if ',' in tArtist:
                tArtist = tArtist.split(',')
            else:
                tArtist = [tArtist]
            tArtist = [artist] + tArtist
        else:
            tArtist = [artist]

        tracks.append(Track(
            title=tTitle,
            duration=tDuration,
            artist=tArtist,
            release_year=int(release_year)
        ))

    albums.append(Album(
        title=title,
        release_year=release_year,
        artist=artist,
        tracks=tracks
    ))


while True:
    print()
    print('Список альбомов:')
    for album in albums:
        print(f'[{albums.index(album)}]: {album}')

    album_choice = int(input('Выберите альбом:'))
    print()
    print(repr(albums[album_choice]))

    print('[0] - Просмотреть трек\n'
          '[1] - Назад')
    choice = int(input('Выберите действие: '))
    print()

    if choice == 0:
        track_choice = int(input('Введите номер трека: '))
        print(repr(albums[album_choice].tracks[track_choice]))
        print()

        print('[0] - Воспроизвести трек\n'
              '[1] - Поставить трек на паузу\n'
              '[2] - Остановить трек'
              '[3] - Выход')
        choice = int(input('Выберите действие: '))
        if choice == 0:
            albums[album_choice].tracks[track_choice].play()
            print('Трек воспроизводится.')
        elif choice == 1:
            albums[album_choice].tracks[track_choice].pause()
            print('Трек поставлен на паузу.')
        elif choice == 2:
            albums[album_choice].tracks[track_choice].stop()
            print('Трек остановлен.')
        else:
            continue
    else:
        continue
