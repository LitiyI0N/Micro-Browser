import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MicroBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Micro Browser")
        self.resize(1024, 768)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        nav_layout = QHBoxLayout()

        self.back_btn = QPushButton("◀")
        self.forward_btn = QPushButton("▶")
        self.reload_btn = QPushButton("⟳")
        self.url_bar = QLineEdit()
        self.go_btn = QPushButton("Go")

        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addWidget(self.reload_btn)
        nav_layout.addWidget(self.url_bar)
        nav_layout.addWidget(self.go_btn)

        main_layout.addLayout(nav_layout)

        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.google.com"))
        main_layout.addWidget(self.web_view)

        self.back_btn.clicked.connect(self.web_view.back)
        self.forward_btn.clicked.connect(self.web_view.forward)
        self.reload_btn.clicked.connect(self.web_view.reload)
        self.go_btn.clicked.connect(self.navigate_to_url)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.web_view.urlChanged.connect(self.update_url_bar)
        self.web_view.titleChanged.connect(self.update_title)

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.web_view.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self, title):
        self.setWindowTitle(f"{title} - Micro Browser")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = MicroBrowser()
    browser.show()
    sys.exit(app.exec_())
