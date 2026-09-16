history = []


def add_to_history(role: str, message: str):
    history.append({
        "role": role,
        "message": message
    })


def get_history() -> list:
    return history


def clear_history():
    history.clear()