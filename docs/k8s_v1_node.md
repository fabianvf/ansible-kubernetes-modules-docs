
## k8s_v1_node

Kubernetes Node

Author: OpenShift (@openshift)

Version added: 2.3.0





---
### Requirements

* kubernetes == 3.0.0




---

  * Synopsis
* Options

* Examples

* Return



#### Synopsis
Manage the lifecycle of a node object. Supports check mode, and attempts to to be idempotent.


#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
| username  |   |  | |  Provide a username for connecting to the API.  |
| ssl_ca_cert  |   |  | |  Path to a CA certificate used to authenticate with the API.  |
| force  |   |  False  | |  If set to C(True), and I(state) is C(present), an existing object will updated, and lists will be replaced, rather than merged.  |
| cert_file  |   |  | |  Path to a certificate used to authenticate with the API.  |
| labels  |   |  | |  Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services.  |
| verify_ssl  |   |  | |  Whether or not to verify the API server's SSL certificates.  |
| spec_provider_id  |   |  | |  ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>  |
| spec_external_id  |   |  | |  External ID of the node assigned by some machine database (e.g. a cloud provider). Deprecated.  |
| kubeconfig  |   |  | |  Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json).  |
| src  |   |  | |  Provide a path to a file containing the YAML definition of the object. Mutually exclusive with I(resource_definition).  |
| password  |   |  | |  Provide a password for connecting to the API. Use in conjunction with I(username).  |
| spec_pod_cidr  |   |  | |  PodCIDR represents the pod IP range assigned to the node.  |
| name  |   |  | |  Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated.  |
| spec_unschedulable  |   |  | |  Unschedulable controls node schedulability of new pods. By default, node is schedulable.  |
| namespace  |   |  | |  Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated.  |
| host  |   |  | |  Provide a URL for acessing the Kubernetes API.  |
| resource_definition  |   |  | |  Provide the YAML definition for the object, bypassing any modules parameters intended to define object attributes.  |
| state  |   |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Determines if an object should be created, patched, or deleted. When set to C(present), the object will be created, if it does not exist, or patched, if parameter values differ from the existing object's attributes, and deleted, if set to C(absent). A patch operation results in merging lists and updating dictionaries, with lists being merged into a unique set of values. If a list contains a dictionary with a I(name) or I(type) attribute, a strategic merge is performed, where individual elements with a matching I(name_) or I(type) are merged. To force the replacement of lists, set the I(force) option to C(True).  |
| context  |   |  | |  The name of a context found in the Kubernetes config file.  |
| debug  |   |  False  | |  Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log  |
| key_file  |   |  | |  Path to a key file used to authenticate with the API.  |
| api_key  |   |  | |  Token used to connect to the API.  |
| spec_taints  |   |  | |  If specified, the node's taints.  |
| annotations  |   |  | |  Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.  |







#### Examples

```





```




#### Return

```yaml

api_version:
  type: string
  description: Requested API version
node:
  type: complex
  returned: when I(state) = C(present)
  contains:
    api_version:
      description:
      - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values.
      type: str
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
      type: str
    metadata:
      description:
      - Standard object's metadata.
      type: complex
      contains:
        annotations:
          description:
          - Annotations is an unstructured key value map stored with a resource that
            may be set by external tools to store and retrieve arbitrary metadata.
            They are not queryable and should be preserved when modifying objects.
          type: complex
          contains: str, str
        cluster_name:
          description:
          - The name of the cluster which the object belongs to. This is used to distinguish
            resources with same name and namespace in different clusters. This field
            is not set anywhere right now and apiserver is going to ignore it if set
            in create or update request.
          type: str
        creation_timestamp:
          description:
          - CreationTimestamp is a timestamp representing the server time when this
            object was created. It is not guaranteed to be set in happens-before order
            across separate operations. Clients may not set this value. It is represented
            in RFC3339 form and is in UTC. Populated by the system. Read-only. Null
            for lists.
          type: complex
          contains: {}
        deletion_grace_period_seconds:
          description:
          - Number of seconds allowed for this object to gracefully terminate before
            it will be removed from the system. Only set when deletionTimestamp is
            also set. May only be shortened. Read-only.
          type: int
        deletion_timestamp:
          description:
          - DeletionTimestamp is RFC 3339 date and time at which this resource will
            be deleted. This field is set by the server when a graceful deletion is
            requested by the user, and is not directly settable by a client. The resource
            is expected to be deleted (no longer visible from resource lists, and
            not reachable by name) after the time in this field. Once set, this value
            may not be unset or be set further into the future, although it may be
            shortened or the resource may be deleted prior to this time. For example,
            a user may request that a pod is deleted in 30 seconds. The Kubelet will
            react by sending a graceful termination signal to the containers in the
            pod. After that 30 seconds, the Kubelet will send a hard termination signal
            (SIGKILL) to the container and after cleanup, remove the pod from the
            API. In the presence of network partitions, this object may still exist
            after this timestamp, until an administrator or automated process can
            determine the resource is fully terminated. If not set, graceful deletion
            of the object has not been requested. Populated by the system when a graceful
            deletion is requested. Read-only.
          type: complex
          contains: {}
        finalizers:
          description:
          - Must be empty before the object is deleted from the registry. Each entry
            is an identifier for the responsible component that will remove the entry
            from the list. If the deletionTimestamp of the object is non-nil, entries
            in this list can only be removed.
          type: list
          contains: str
        generate_name:
          description:
          - GenerateName is an optional prefix, used by the server, to generate a
            unique name ONLY IF the Name field has not been provided. If this field
            is used, the name returned to the client will be different than the name
            passed. This value will also be combined with a unique suffix. The provided
            value has the same validation rules as the Name field, and may be truncated
            by the length of the suffix required to make the value unique on the server.
            If this field is specified and the generated name exists, the server will
            NOT return a 409 - instead, it will either return 201 Created or 500 with
            Reason ServerTimeout indicating a unique name could not be found in the
            time allotted, and the client should retry (optionally after the time
            indicated in the Retry-After header). Applied only if Name is not specified.
          type: str
        generation:
          description:
          - A sequence number representing a specific generation of the desired state.
            Populated by the system. Read-only.
          type: int
        initializers:
          description:
          - An initializer is a controller which enforces some system invariant at
            object creation time. This field is a list of initializers that have not
            yet acted on this object. If nil or empty, this object has been completely
            initialized. Otherwise, the object is considered uninitialized and is
            hidden (in list/watch and get calls) from clients that haven't explicitly
            asked to observe uninitialized objects. When an object is created, the
            system will populate this list with the current set of initializers. Only
            privileged users may set or modify this list. Once it is empty, it may
            not be modified further by any user.
          type: complex
          contains:
            pending:
              description:
              - Pending is a list of initializers that must execute in order before
                this object is visible. When the last pending initializer is removed,
                and no failing result is set, the initializers struct will be set
                to nil and the object is considered as initialized and visible to
                all clients.
              type: list
              contains:
                name:
                  description:
                  - name of the process that is responsible for initializing this
                    object.
                  type: str
            result:
              description:
              - If result is set with the Failure field, the object will be persisted
                to storage and then deleted, ensuring that other clients can observe
                the deletion.
              type: complex
              contains:
                api_version:
                  description:
                  - APIVersion defines the versioned schema of this representation
                    of an object. Servers should convert recognized schemas to the
                    latest internal value, and may reject unrecognized values.
                  type: str
                code:
                  description:
                  - Suggested HTTP return code for this status, 0 if not set.
                  type: int
                details:
                  description:
                  - Extended data associated with the reason. Each reason may define
                    its own extended details. This field is optional and the data
                    returned is not guaranteed to conform to any schema except that
                    defined by the reason type.
                  type: complex
                  contains:
                    causes:
                      description:
                      - The Causes array includes more details associated with the
                        StatusReason failure. Not all StatusReasons may provide detailed
                        causes.
                      type: list
                      contains:
                        field:
                          description:
                          - 'The field of the resource that has caused this error,
                            as named by its JSON serialization. May include dot and
                            postfix notation for nested attributes. Arrays are zero-indexed.
                            Fields may appear more than once in an array of causes
                            due to fields having multiple errors. Optional. Examples:
                            "name" - the field "name" on the current resource "items[0].name"
                            - the field "name" on the first array entry in "items"'
                          type: str
                        message:
                          description:
                          - A human-readable description of the cause of the error.
                            This field may be presented as-is to a reader.
                          type: str
                        reason:
                          description:
                          - A machine-readable description of the cause of the error.
                            If this value is empty there is no information available.
                          type: str
                    group:
                      description:
                      - The group attribute of the resource associated with the status
                        StatusReason.
                      type: str
                    kind:
                      description:
                      - The kind attribute of the resource associated with the status
                        StatusReason. On some operations may differ from the requested
                        resource Kind.
                      type: str
                    name:
                      description:
                      - The name attribute of the resource associated with the status
                        StatusReason (when there is a single name which can be described).
                      type: str
                    retry_after_seconds:
                      description:
                      - If specified, the time in seconds before the operation should
                        be retried.
                      type: int
                    uid:
                      description:
                      - UID of the resource. (when there is a single resource which
                        can be described).
                      type: str
                kind:
                  description:
                  - Kind is a string value representing the REST resource this object
                    represents. Servers may infer this from the endpoint the client
                    submits requests to. Cannot be updated. In CamelCase.
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
                      - String that identifies the server's internal version of this
                        object that can be used by clients to determine when objects
                        have changed. Value must be treated as opaque by clients and
                        passed unmodified back to the server. Populated by the system.
                        Read-only.
                      type: str
                    self_link:
                      description:
                      - SelfLink is a URL representing this object. Populated by the
                        system. Read-only.
                      type: str
                reason:
                  description:
                  - A machine-readable description of why this operation is in the
                    "Failure" status. If this value is empty there is no information
                    available. A Reason clarifies an HTTP status code but does not
                    override it.
                  type: str
                status:
                  description:
                  - 'Status of the operation. One of: "Success" or "Failure".'
                  type: str
        labels:
          description:
          - Map of string keys and values that can be used to organize and categorize
            (scope and select) objects. May match selectors of replication controllers
            and services.
          type: complex
          contains: str, str
        name:
          description:
          - Name must be unique within a namespace. Is required when creating resources,
            although some resources may allow a client to request the generation of
            an appropriate name automatically. Name is primarily intended for creation
            idempotence and configuration definition. Cannot be updated.
          type: str
        namespace:
          description:
          - Namespace defines the space within each name must be unique. An empty
            namespace is equivalent to the "default" namespace, but "default" is the
            canonical representation. Not all objects are required to be scoped to
            a namespace - the value of this field for those objects will be empty.
            Must be a DNS_LABEL. Cannot be updated.
          type: str
        owner_references:
          description:
          - List of objects depended by this object. If ALL objects in the list have
            been deleted, this object will be garbage collected. If this object is
            managed by a controller, then an entry in this list will point to this
            controller, with the controller field set to true. There cannot be more
            than one managing controller.
          type: list
          contains:
            api_version:
              description:
              - API version of the referent.
              type: str
            block_owner_deletion:
              description:
              - If true, AND if the owner has the "foregroundDeletion" finalizer,
                then the owner cannot be deleted from the key-value store until this
                reference is removed. Defaults to false. To set this field, a user
                needs "delete" permission of the owner, otherwise 422 (Unprocessable
                Entity) will be returned.
              type: bool
            controller:
              description:
              - If true, this reference points to the managing controller.
              type: bool
            kind:
              description:
              - Kind of the referent.
              type: str
            name:
              description:
              - Name of the referent.
              type: str
            uid:
              description:
              - UID of the referent.
              type: str
        resource_version:
          description:
          - An opaque value that represents the internal version of this object that
            can be used by clients to determine when objects have changed. May be
            used for optimistic concurrency, change detection, and the watch operation
            on a resource or set of resources. Clients must treat these values as
            opaque and passed unmodified back to the server. They may only be valid
            for a particular resource or set of resources. Populated by the system.
            Read-only. Value must be treated as opaque by clients and .
          type: str
        self_link:
          description:
          - SelfLink is a URL representing this object. Populated by the system. Read-only.
          type: str
        uid:
          description:
          - UID is the unique in time and space value for this object. It is typically
            generated by the server on successful creation of a resource and is not
            allowed to change on PUT operations. Populated by the system. Read-only.
          type: str
    spec:
      description:
      - Spec defines the behavior of a node.
      type: complex
      contains:
        external_id:
          description:
          - External ID of the node assigned by some machine database (e.g. a cloud
            provider). Deprecated.
          type: str
        pod_cidr:
          description:
          - PodCIDR represents the pod IP range assigned to the node.
          type: str
        provider_id:
          description:
          - 'ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>'
          type: str
        taints:
          description:
          - If specified, the node's taints.
          type: list
          contains:
            effect:
              description:
              - Required. The effect of the taint on pods that do not tolerate the
                taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.
              type: str
            key:
              description:
              - Required. The taint key to be applied to a node.
              type: str
            time_added:
              description:
              - TimeAdded represents the time at which the taint was added. It is
                only written for NoExecute taints.
              type: complex
              contains: {}
            value:
              description:
              - Required. The taint value corresponding to the taint key.
              type: str
        unschedulable:
          description:
          - Unschedulable controls node schedulability of new pods. By default, node
            is schedulable.
          type: bool
    status:
      description:
      - Most recently observed status of the node. Populated by the system. Read-only.
      type: complex
      contains:
        addresses:
          description:
          - List of addresses reachable to the node. Queried from cloud provider,
            if available.
          type: list
          contains:
            address:
              description:
              - The node address.
              type: str
            type:
              description:
              - Node address type, one of Hostname, ExternalIP or InternalIP.
              type: str
        allocatable:
          description:
          - Allocatable represents the resources of a node that are available for
            scheduling. Defaults to Capacity.
          type: complex
          contains: str, str
        capacity:
          description:
          - Capacity represents the total resources of a node.
          type: complex
          contains: str, str
        conditions:
          description:
          - Conditions is an array of current observed node conditions.
          type: list
          contains:
            last_heartbeat_time:
              description:
              - Last time we got an update on a given condition.
              type: complex
              contains: {}
            last_transition_time:
              description:
              - Last time the condition transit from one status to another.
              type: complex
              contains: {}
            message:
              description:
              - Human readable message indicating details about last transition.
              type: str
            reason:
              description:
              - (brief) reason for the condition's last transition.
              type: str
            status:
              description:
              - Status of the condition, one of True, False, Unknown.
              type: str
            type:
              description:
              - Type of node condition.
              type: str
        daemon_endpoints:
          description:
          - Endpoints of daemons running on the Node.
          type: complex
          contains:
            kubelet_endpoint:
              description:
              - Endpoint on which Kubelet is listening.
              type: complex
              contains:
                port:
                  description:
                  - Port number of the given endpoint.
                  type: int
        images:
          description:
          - List of container images on this node
          type: list
          contains:
            names:
              description:
              - Names by which this image is known. e.g. ["gcr.io/google_containers/hyperkube:v1.0.7",
                "dockerhub.io/google_containers/hyperkube:v1.0.7"]
              type: list
              contains: str
            size_bytes:
              description:
              - The size of the image in bytes.
              type: int
        node_info:
          description:
          - Set of ids/uuids to uniquely identify the node.
          type: complex
          contains:
            architecture:
              description:
              - The Architecture reported by the node
              type: str
            boot_id:
              description:
              - Boot ID reported by the node.
              type: str
            container_runtime_version:
              description:
              - ContainerRuntime Version reported by the node through runtime remote
                API (e.g. docker://1.5.0).
              type: str
            kernel_version:
              description:
              - Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).
              type: str
            kube_proxy_version:
              description:
              - KubeProxy Version reported by the node.
              type: str
            kubelet_version:
              description:
              - Kubelet Version reported by the node.
              type: str
            machine_id:
              description:
              - 'MachineID reported by the node. For unique machine identification
                in the cluster this field is preferred. Learn more from man(5) machine-id:
                http://man7.org/linux/man-pages/man5/machine-id.5.html'
              type: str
            operating_system:
              description:
              - The Operating System reported by the node
              type: str
            os_image:
              description:
              - OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux
                7 (wheezy)).
              type: str
            system_uuid:
              description:
              - SystemUUID reported by the node. For unique machine identification
                MachineID is preferred. This field is specific to Red Hat hosts
              type: str
        phase:
          description:
          - NodePhase is the recently observed lifecycle phase of the node.
          type: str
        volumes_attached:
          description:
          - List of volumes that are attached to the node.
          type: list
          contains:
            device_path:
              description:
              - DevicePath represents the device path where the volume should be available
              type: str
            name:
              description:
              - Name of the attached volume
              type: str
        volumes_in_use:
          description:
          - List of attachable volumes in use (mounted) by the node.
          type: list
          contains: str

```





---