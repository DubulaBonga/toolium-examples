# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from selenium.webdriver.common.by import By

from toolium_examples.pageobjects.android.drag_and_drop import DragAndDropPageObject
from toolium_examples.pageobjects.android.menu import MenuPageObject
from toolium_examples.test_cases import AndroidTestCase


class Gestures(AndroidTestCase):
    def test_drag_and_drop(self):
        # Open drag_and_drop activity
        MenuPageObject().open_option('Views').open_option('Drag and Drop')
        drag_and_drop_page = DragAndDropPageObject()

        # Drag and drop an element into another
        drag_and_drop_page.drag_and_drop()

        # Check movement
        result = self.driver.find_element_by_id('io.appium.android.apis:id/drag_result_text')
        self.assertEqual('Dropped!', drag_and_drop_page.result.text)

    def test_swipe_simple(self):
        self.driver.swipe(50, 400, 50, 200, 500)

    def test_swipe(self):
        views_element = None
        for i in range(10):
            elements = self.driver.find_elements(By.XPATH, "//*[@text='Views']")
            if len(elements) > 0:
                views_element = elements[0]
                break
            self.driver.swipe(50, 400, 50, 200, 500)
        self.assertIsNotNone(views_element)
        views_element.click()
