import clr
import os.path
import time

# project_dir = os.path.dirname(os.path.abspath(__file__))
import sys

from conftest import project_dir

sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *


class MainHelper:

    def __init__(self, app):
        self.app = app

    def open_group_editor(self):
        self.app.main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = self.app.main_window.ModalWindow("Group editor")
        return modal

    def ensure_modals_closed(self):
        modals = self.app.main_window.ModalWindows()
        if len(modals) > 0:
            modals[0].Close()

    def exit(self):
        self.app.main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()
