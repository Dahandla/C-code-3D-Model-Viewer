import sys

# Import your compiled module (now CcodeGLB_Viewer_v1_3)
import Ccode3D_Viewer_v1_3

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    viewer = Ccode3D_Viewer_v1_3.ModelViewer()
    viewer.show()
    sys.exit(app.exec())