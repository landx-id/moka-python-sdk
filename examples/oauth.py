from moka_python_sdk.moka import Moka


API_KEY = "test_f7f7955d44cd10dd2bbbdc4381eb8d4c"
SECRET_KEY = "d269d087-25a6-49fa-b17c-22cd1b23c515"
x = Moka(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

oauth = x.Oauth



print("Refresh Token:")
print(oauth.refresh_token(
    refresh_token="4037144d6e0b191ae42490a2758cf9989",
    client_id="7a5a83adb069d27563e0d67882a1e0b0739f0eaf",
    client_secret="4fc78952dde155d350d93603c2b0f542a8b371aeb014"
))

print("Get Access Token:")
print(oauth.get_access_token(
    code="1231232134037144d6e0b191ae42490a2758cf9989",
    client_id="7a5a83adb069d27563e0d67882a1e0b0739f0eaf",
    client_secret="4fc78952dde155d350d93603c2b0f542a8b371aeb014",
    redirect_uri="http://localhost:5002/auth/moka/callback"
))



print("Revoke Token: ")
print(oauth.revoke_token(
    client_id="7a5a83adb069d27563e0d67882a1e0b0739f0eaf",
    client_secret="4fc78952dde155d350d93603c2b0f542a8b371aeb014",
    token="vbnm123465789qwertyuiopasdfghkjlzxc"
))