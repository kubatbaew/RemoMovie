def media_path(instance, filename, media_type, type):
    if type == 'movie':
        return f"{instance.movie.title}/media/{media_type}/{filename}"

    if type == 'celebrity':
        return f"{instance.celebrity.full_name}/media/{media_type}/{filename}"


def upload_to_image_for_movie(instance, filename):
    return media_path(instance, filename, 'image', type='movie')


def upload_to_video_for_movie(instance, filename):
    return media_path(instance, filename, 'video', type='movie')


def upload_to_image_for_celebrity(instance, filename):
    return media_path(instance, filename, 'image', type='celebrity')


def upload_to_image_for_director(instance, filename):
    return media_path(instance, filename, 'image', type='celebrity')
