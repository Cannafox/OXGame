from static import StatusCode
from app import App


def run() -> StatusCode:
    print("Running...")
    app = App()
    app.mainloop()

    return StatusCode.SUCCESS


if __name__ == "__main__":
    status = run()

    print(f"Finished, status {status.name}")
