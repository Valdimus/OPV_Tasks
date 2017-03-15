# coding: utf-8

# Copyright (C) 2017 Open Path View, Maison Du Libre
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

# Contributors: Christophe NOUCHET <christophe.nouchet@openpathview.fr>
# Email: team@openpathview.fr
# Description: Abstract class for representing task, you must redefine the run methods.

from opv_tasks import Task
from opv_tasks import run_cli


import json


class ExampleTask(Task):
    """Example task."""

    def run(self, options={}):
        """
        Run the task.

        :param options: Options to use
        :return:
        :raise
        """
        print("On fait ce qu'on a faire ici")
        run_cli("echo", ["Bijour les amis"])
        run_cli(["ls", "-lah"])
        return json.dumps({})
