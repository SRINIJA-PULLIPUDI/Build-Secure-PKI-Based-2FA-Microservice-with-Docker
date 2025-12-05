from crypto_utils import load_private_key, decrypt_seed

private_key = load_private_key("student_private.pem")

encrypted_seed = """
a1LsHO+m3fVLotdLTeqVr4ckpKynSoKVXBCKeHgjPADV32j1hJfvmLQ8vpCeMwvNRoixa47uUxSsqOlsFKfrEgqBRZtd5NI/3cvWOmW+3XOs27SJHaStTX029g/VZsXtkIL/22MXB5tzuHSCk5qwcrMOie539wMvDWJy55fgab/Y+SsUjobCej4s/+QCpaX+YfrSrYISIAGegnC7iWkd95GybWU1HAsSDlZN3ZIgimmPt/421i83pzhzewoH049PKMBx+Y2Ww+a/WnFo7Iqkprp8yt1JVuTnvEDdayWpxEdp+WHFnWg4sSyFtspA4aGm2IJB9NvqTY4GMtQzn3jAo4tztLCxzPxeu3Tgx2qWJdWQCpkUJkm5uNjvs3B+x4nQ/vTDDYuxvo7owlelV4Bb+dfFfdkMbhJ5vxQkRCDG481qvSs6gHXzHUVdiFXq7Ct3L4kWfzHBMWhRGZ62D/N9HWbnxA8tRBYBiHiDGYvpV8kSUS1AbdqaWyEY/fWBrjcMeHIZDrwLMkn1Qbslq3zDRX2MlCXD1LeBHGCekNe0eprp9sCrGxMapSVknSGv/QEyXSxDB4mcwjUg1acFcTgRsabuujoQyGVC0yz3/M+Tm+CBDxBI/esooegBNZT0DuGEf/UGntmxR2mjSe425CXPOy0ehS9hPdIol5zkCA8/P00=
"""

encrypted_seed = encrypted_seed.strip()

try:
    seed = decrypt_seed(encrypted_seed, private_key)
    print("Decrypted seed:", seed)
except Exception as e:
    print("Error:", e)
