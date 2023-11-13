
from fastapi import HTTPException, status

UserAlreadyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='User already exist'
)

IncorrentEmalOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='not valid user or password'
)

TokenExpiresException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='token expire'
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='token not exist'
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='incorrect token format'
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_409_CONFLICT
)
