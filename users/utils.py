from django.core.exceptions import ValidationError
import magic

def validate_uploaded_file(file):
    """ 
        This function is used to validate if an uploaded file is an audio, image or video. The function validates if the user has uploaded a valid audio, image or video file.

        ---------------------------------------------------------------------------- 
                                ACCEPTED FILE EXTENSIONS
        ----------------------------------------------------------------------------

        Audio file extensions: .3gp, .mp3, .opus & .wav
        Image file extensions: .jpg, .jpeg & .png
        Video file extensions: .3gp, .mp4, & .mpeg & .ogv
    """
    accept = [
        'audio/mpeg',
        'audio/ogg',
        'audio/opus',
        'audio/wav',
        'image/jpg',
        'image/jpeg',
        'image/png',
        'video/mp4',
        'video/mpeg',
        'video/ogg',
        'video/3gpp; audio/3gpp',   # if it doesn't contain video.
    
    ]
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)

    if file_mime_type not in accept:
        raise ValidationError('Unsupported file format!')