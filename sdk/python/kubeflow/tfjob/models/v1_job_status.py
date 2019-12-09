# Copyright 2019 kubeflow.org.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    tfjob

    Python SDK for TF-Operator  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client import V1JobCondition  # noqa: F401,E501
from kubeflow.tfjob.models.v1_replica_status import V1ReplicaStatus  # noqa: F401,E501
from kubeflow.tfjob.models.v1_time import V1Time  # noqa: F401,E501


class V1JobStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'completion_time': 'V1Time',
        'conditions': 'list[V1JobCondition]',
        'last_reconcile_time': 'V1Time',
        'replica_statuses': 'dict(str, V1ReplicaStatus)',
        'start_time': 'V1Time'
    }

    attribute_map = {
        'completion_time': 'completionTime',
        'conditions': 'conditions',
        'last_reconcile_time': 'lastReconcileTime',
        'replica_statuses': 'replicaStatuses',
        'start_time': 'startTime'
    }

    def __init__(self, completion_time=None, conditions=None, last_reconcile_time=None, replica_statuses=None, start_time=None):  # noqa: E501
        """V1JobStatus - a model defined in Swagger"""  # noqa: E501

        self._completion_time = None
        self._conditions = None
        self._last_reconcile_time = None
        self._replica_statuses = None
        self._start_time = None
        self.discriminator = None

        if completion_time is not None:
            self.completion_time = completion_time
        self.conditions = conditions
        if last_reconcile_time is not None:
            self.last_reconcile_time = last_reconcile_time
        self.replica_statuses = replica_statuses
        if start_time is not None:
            self.start_time = start_time

    @property
    def completion_time(self):
        """Gets the completion_time of this V1JobStatus.  # noqa: E501

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The completion_time of this V1JobStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this V1JobStatus.

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param completion_time: The completion_time of this V1JobStatus.  # noqa: E501
        :type: V1Time
        """

        self._completion_time = completion_time

    @property
    def conditions(self):
        """Gets the conditions of this V1JobStatus.  # noqa: E501

        Conditions is an array of current observed job conditions.  # noqa: E501

        :return: The conditions of this V1JobStatus.  # noqa: E501
        :rtype: list[V1JobCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1JobStatus.

        Conditions is an array of current observed job conditions.  # noqa: E501

        :param conditions: The conditions of this V1JobStatus.  # noqa: E501
        :type: list[V1JobCondition]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")  # noqa: E501

        self._conditions = conditions

    @property
    def last_reconcile_time(self):
        """Gets the last_reconcile_time of this V1JobStatus.  # noqa: E501

        Represents last time when the job was reconciled. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The last_reconcile_time of this V1JobStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._last_reconcile_time

    @last_reconcile_time.setter
    def last_reconcile_time(self, last_reconcile_time):
        """Sets the last_reconcile_time of this V1JobStatus.

        Represents last time when the job was reconciled. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param last_reconcile_time: The last_reconcile_time of this V1JobStatus.  # noqa: E501
        :type: V1Time
        """

        self._last_reconcile_time = last_reconcile_time

    @property
    def replica_statuses(self):
        """Gets the replica_statuses of this V1JobStatus.  # noqa: E501

        ReplicaStatuses is map of ReplicaType and ReplicaStatus, specifies the status of each replica.  # noqa: E501

        :return: The replica_statuses of this V1JobStatus.  # noqa: E501
        :rtype: dict(str, V1ReplicaStatus)
        """
        return self._replica_statuses

    @replica_statuses.setter
    def replica_statuses(self, replica_statuses):
        """Sets the replica_statuses of this V1JobStatus.

        ReplicaStatuses is map of ReplicaType and ReplicaStatus, specifies the status of each replica.  # noqa: E501

        :param replica_statuses: The replica_statuses of this V1JobStatus.  # noqa: E501
        :type: dict(str, V1ReplicaStatus)
        """
        if replica_statuses is None:
            raise ValueError("Invalid value for `replica_statuses`, must not be `None`")  # noqa: E501

        self._replica_statuses = replica_statuses

    @property
    def start_time(self):
        """Gets the start_time of this V1JobStatus.  # noqa: E501

        Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The start_time of this V1JobStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1JobStatus.

        Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param start_time: The start_time of this V1JobStatus.  # noqa: E501
        :type: V1Time
        """

        self._start_time = start_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1JobStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1JobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
