#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#                 Bebe <florin.strugariu@softvision.ro>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

'''
This class is used to access  all the enumerations in the AMO pages.

Usage:

Create a class with the area name that will inherit the Item class ex:

class Results (AddonsBasePage, Item):

add a constuctor for that class ex:

         def __init__(self, testsetup, locator, lookup):
            AddonsBasePage.__init__(self, testsetup)
            self.locator = locator        #enumeration root locator
            self.lookup = lookup          # Item Number or Name

Access the Items with:
    List of all Items:
        results = [Results(self.testsetup, self._results_locator, i) for i in range(self.results_count)]
    One item by number or name:
        result = Results(self.testsetup, self._results_locator, 1)
        result = Results(self.testsetup, self._results_locator, 'First Item')
'''


class Item:

    def absolute_locator(self, relative_locator):
        return self._root_locator + relative_locator

    @property
    def _root_locator(self):
        if type(self.lookup) == int:
            # lookup by index
            return "%s:nth(%s) " % (self.locator, self.lookup)
        else:
            # lookup by name
            return "%s:contains(%s) " % (self.locator, self.lookup)
