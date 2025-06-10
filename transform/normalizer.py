from datetime import datetime
import hashlib

def sha256_encrypt(value):
    """Nếu cần thêm vào các trường cần bảo mật"""
    if value:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()
    return None

def normalize_sql_data(sql_records):
    normalized = []
    for r in sql_records:
        normalized.append({
            "id": f"sql_{r['id']}",
            "name": r["name"],
            "email": r["email"].strip().lower() if r.get("email") else None,
            "phone": r["phone"].strip() if r.get("phone") else None,
            "created_at": r["created_at"],
            "source": "sql"
        })
    return normalized

def normalize_api_data(api_records):
    normalized = []
    for r in api_records:
        normalized.append({
            "id": r.get("customerId", "unknown"),
            "name": r.get("fullName"),
            "email": r.get("contact", {}).get("email", "").strip().lower(),
            "phone": r.get("contact", {}).get("phone", "").strip(),
            "created_at": r.get("timestamp", datetime.utcnow().isoformat()),
            "source": "api"
        })
    return normalized

def deduplicate_records(records: list[dict]) -> list[dict]:

    deduplicated = []
    seen_hashes = set()

    for record in records:
        email = record.get("email", "").lower()
        phone = record.get("phone", "")
        key = f"{email}|{phone}"

        record_hash = hashlib.md5(key.encode("utf-8")).hexdigest()

        if record_hash not in seen_hashes:
            seen_hashes.add(record_hash)
            deduplicated.append(record)
        else:
            print(f"Đã tồn tại: {record['email']} - {record['phone']}")

    return deduplicated
