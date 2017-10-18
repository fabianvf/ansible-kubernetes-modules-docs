
## k8s_v1_status

Kubernetes Status

Author: OpenShift (@openshift)

Version added: 2.3.0





---
### Requirements

* kubernetes == 3.0.0




---

  * Synopsis
  * Options
  * Examples

#### Synopsis
Manage the lifecycle of a status object. Supports check mode, and attempts to to be idempotent.


#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |

| username  |     |    | <ul></ul> |  Provide a username for connecting to the API.  |

| ssl_ca_cert  |     |    | <ul></ul> |  Path to a CA certificate used to authenticate with the API.  |

| code  |     |    | <ul></ul> |  Suggested HTTP return code for this status, 0 if not set.  |

| force  |     |  False  | <ul></ul> |  If set to C(True), and I(state) is C(present), an existing object will updated, and lists will be replaced, rather than merged.  |

| details_uid  |     |    | <ul></ul> |  UID of the resource. (when there is a single resource which can be described).  |

| cert_file  |     |    | <ul></ul> |  Path to a certificate used to authenticate with the API.  |

| verify_ssl  |     |    | <ul></ul> |  Whether or not to verify the API server's SSL certificates.  |

| details_causes  |     |    | <ul></ul> |  The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.  |

| host  |     |    | <ul></ul> |  Provide a URL for acessing the Kubernetes API.  |

| message  |     |    | <ul></ul> |  A human-readable description of the status of this operation.  |

| password  |     |    | <ul></ul> |  Provide a password for connecting to the API. Use in conjunction with I(username).  |

| details_retry_after_seconds  |     |    | <ul></ul> |  If specified, the time in seconds before the operation should be retried.  |

| details_kind  |     |    | <ul></ul> |  The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind.  |

| details_name  |     |    | <ul></ul> |  The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).  |

| reason  |     |    | <ul></ul> |  A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.  |

| kubeconfig  |     |    | <ul></ul> |  Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json).  |

| context  |     |    | <ul></ul> |  The name of a context found in the Kubernetes config file.  |

| debug  |     |  False  | <ul></ul> |  Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log  |

| key_file  |     |    | <ul></ul> |  Path to a key file used to authenticate with the API.  |

| api_key  |     |    | <ul></ul> |  Token used to connect to the API.  |

| details_group  |     |    | <ul></ul> |  The group attribute of the resource associated with the status StatusReason.  |









#### Return

```yaml
api_version:
  type: string
  description: Requested API version
status:
  type: complex
  returned: on success
  contains:
    api_version:
      description:
      - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values.
      type: str
    code:
      description:
      - Suggested HTTP return code for this status, 0 if not set.
      type: int
    details:
      description:
      - Extended data associated with the reason. Each reason may define its own extended
        details. This field is optional and the data returned is not guaranteed to
        conform to any schema except that defined by the reason type.
      type: complex
      contains:
        causes:
          description:
          - The Causes array includes more details associated with the StatusReason
            failure. Not all StatusReasons may provide detailed causes.
          type: list
          contains:
            field:
              description:
              - 'The field of the resource that has caused this error, as named by
                its JSON serialization. May include dot and postfix notation for nested
                attributes. Arrays are zero-indexed. Fields may appear more than once
                in an array of causes due to fields having multiple errors. Optional.
                Examples: "name" - the field "name" on the current resource "items[0].name"
                - the field "name" on the first array entry in "items"'
              type: str
            message:
              description:
              - A human-readable description of the cause of the error. This field
                may be presented as-is to a reader.
              type: str
            reason:
              description:
              - A machine-readable description of the cause of the error. If this
                value is empty there is no information available.
              type: str
        group:
          description:
          - The group attribute of the resource associated with the status StatusReason.
          type: str
        kind:
          description:
          - The kind attribute of the resource associated with the status StatusReason.
            On some operations may differ from the requested resource Kind.
          type: str
        name:
          description:
          - The name attribute of the resource associated with the status StatusReason
            (when there is a single name which can be described).
          type: str
        retry_after_seconds:
          description:
          - If specified, the time in seconds before the operation should be retried.
          type: int
        uid:
          description:
          - UID of the resource. (when there is a single resource which can be described).
          type: str
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
      type: str
    message:
      description:
      - A human-readable description of the status of this operation.
      type: str
    metadata:
      description:
      - Standard list metadata.
      type: complex
      contains:
        resource_version:
          description:
          - String that identifies the server's internal version of this object that
            can be used by clients to determine when objects have changed. Value must
            be treated as opaque by clients and passed unmodified back to the server.
            Populated by the system. Read-only.
          type: str
        self_link:
          description:
          - SelfLink is a URL representing this object. Populated by the system. Read-only.
          type: str
    reason:
      description:
      - A machine-readable description of why this operation is in the "Failure" status.
        If this value is empty there is no information available. A Reason clarifies
        an HTTP status code but does not override it.
      type: str
    status:
      description:
      - 'Status of the operation. One of: "Success" or "Failure".'
      type: str

```





---