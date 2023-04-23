"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_insurance_prices import get_insurance_prices


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Insurance'.
    """

    @property
    def get_insurance_prices(self) -> get_insurance_prices:
        """
        List insurance levels


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Insurance.get_insurance_prices.get_insurance_prices.get_sync`,
        :func:`~EVECelery.tasks.ESI.Insurance.get_insurance_prices.get_insurance_prices.run`, and
        :class:`~EVECelery.tasks.ESI.Insurance.get_insurance_prices.get_insurance_prices`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_insurance_prices()
