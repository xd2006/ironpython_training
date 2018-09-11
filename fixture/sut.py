import clr
import os.path
import time

from conftest import project_dir
from fixture.group import GroupHelper
from fixture.main import MainHelper

import sys

sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application
from TestStack.White.UIItems.Finders import *
clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *



class Sut:

    contact = None  # type: MainHelper
    group = None  # type: GroupHelper

    def __init__(self, app_path):
        self.application = Application.Launch(app_path)
        self.main_window = self.application.GetWindow("Free Address Book")

        self.group = GroupHelper(self)
        self.main = MainHelper(self)

    def destroy(self):
        self.main_window.Close()


    def is_valid(self):
        try:
            self.application.GetWindow("Free Address Book")
            return True
        except:
            return False