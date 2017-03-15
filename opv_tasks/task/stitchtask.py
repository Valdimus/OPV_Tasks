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
# Description: Stitch the panorama

import json
import logging

from path import Path
from .task import Task
from opv_tasks.const import Const

logger = logging.getLogger(__name__)


class StitchTask(Task):
    """Stitch the panorama."""

    TMP_PTONAME = 'tmp.pto'

    def stitch(self, proj_pto):
        """Stitch a projection."""
        self._run_cli('hugin_executor', ["-s", proj_pto])
        with self._opv_directory_manager.Open() as (path_uuid, panorama_path):
            panorama_path = Path(panorama_path)

            pano = proj_pto.dirname().glob('*.tif')[0]
            logger.debug("Moving pano -> %s" % (panorama_path / Const.PANO_FILENAME))
            pano.move(panorama_path / Const.PANO_FILENAME)

            logger.debug("Adding panorama in DB")
            self.panorama = self._client_requestor.Panorama()
            self.panorama.equirectangular_path = path_uuid
            self.panorama.cp = self.cp
            self.panorama.save()

    def run(self, options={}):
        """Run a StitchTask with options."""
        if "id" in options:
            self.cp = self._client_requestor.Cp(options["id"])

            with self._opv_directory_manager.Open(self.cp.pto_dir) as (_, pto_dirpath):
                proj_pto = Path(pto_dirpath) / Const.CP_PTO_FILENAME

                with self._opv_directory_manager.Open(self.cp.lot.pictures_path) as (_, pictures_dir):
                    local_tmp_pto = Path(pictures_dir) / self.TMP_PTONAME

                    logging.debug("Copy pto file " + proj_pto + " -> " + local_tmp_pto)
                    proj_pto.copyfile(local_tmp_pto)

                    self.stitch(local_tmp_pto)

            return json.dumps({"id": self.panorama.id})
