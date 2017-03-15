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

# Contributors: tristan GOUGE <gouge.tristan@openpathview.fr>
# Email: team@openpathview.fr
# Description: Set in db isStichable if needed

import logging
import json

from path import Path
from .task import Task
from hsi import Panorama, ifstream
from opv_tasks.const import Const

logger = logging.getLogger(__name__)


class StitchableTask(Task):
    """Set in db isStichable if needed."""

    def stichable(self, proj_pto):
        """Check if a proj_pto is stichable."""
        ifs = ifstream(proj_pto)

        p = Panorama()
        p.readData(ifs)

        cpv = p.getCtrlPoints()
        picLinkNb = [0 for x in range(6)]
        nbPoints = 0

        for cp in cpv:
            picLinkNb[cp.image1Nr] += 1
            picLinkNb[cp.image2Nr] += 1
            nbPoints += 1
        minLinksNeeded = 4

        isStitchable = all(x > minLinksNeeded for x in picLinkNb)

        self.cp.nb_cp = nbPoints
        self.cp.stichable = isStitchable
        self.cp.save()

    def run(self, options={}):
        """Run a stichable task with options."""
        if "id" in options:
            self.cp = self._client_requestor.Cp(options["id"])
            with self._opv_directory_manager.Open(self.cp.pto_dir) as (_, pto_dirpath):
                proj_pto = Path(pto_dirpath) / Const.CP_PTO_FILENAME

                self.stichable(proj_pto)

            return json.dumps({"id": self.cp.id})
