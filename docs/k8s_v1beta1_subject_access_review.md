
## k8s_v1beta1_subject_access_review

Kubernetes SubjectAccessReview

Author: OpenShift (@openshift)

Version added: 2.3.0





---
### Requirements

* kubernetes == 3.0.0




---

  * [Synopsis](#synopsis)

  * [Options](#options)


* [Return](#return)



#### Synopsis
Manage the lifecycle of a subject_access_review object. Supports check mode, and attempts to to be idempotent.


#### Options

| Parameter     |  aliases     | required    | default  | choices    | comments |
| ------------- |------------- |-------------| ---------|----------- |--------- |
| annotations  |  |   |  | |  Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.  |
| api_key  |  |   |  | |  Token used to connect to the API.  |
| cert_file  |  |   |  | |  Path to a certificate used to authenticate with the API.  |
| context  |  |   |  | |  The name of a context found in the Kubernetes config file.  |
| debug  |  |   |  False  | |  Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log  |
| force  |  |   |  False  | |  If set to C(True), and I(state) is C(present), an existing object will updated, and lists will be replaced, rather than merged.  |
| host  |  |   |  | |  Provide a URL for acessing the Kubernetes API.  |
| key_file  |  |   |  | |  Path to a key file used to authenticate with the API.  |
| kubeconfig  |  |   |  | |  Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json).  |
| labels  |  |   |  | |  Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services.  |
| name  |  |   |  | |  Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated.  |
| namespace  |  |   |  | |  Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated.  |
| password  |  |   |  | |  Provide a password for connecting to the API. Use in conjunction with I(username).  |
| spec_extra  |  extra  |   |  | |  Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer it needs a reflection here.  |
| spec_group  |  group  |   |  | |  Groups is the groups you're testing for.  |
| spec_non_resource_attributes_path  |  non_resource_attributes_path  |   |  | |  Path is the URL path of the request  |
| spec_non_resource_attributes_verb  |  non_resource_attributes_verb  |   |  | |  Verb is the standard HTTP verb  |
| spec_resource_attributes_group  |  resource_attributes_group  |   |  | |  Group is the API Group of the Resource. "*" means all.  |
| spec_resource_attributes_name  |  resource_attributes_name  |   |  | |  Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.  |
| spec_resource_attributes_namespace  |  resource_attributes_namespace  |   |  | |  Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview  |
| spec_resource_attributes_resource  |  resource_attributes_resource  |   |  | |  Resource is one of the existing resource types. "*" means all.  |
| spec_resource_attributes_subresource  |  resource_attributes_subresource  |   |  | |  Subresource is one of the existing resource types. "" means none.  |
| spec_resource_attributes_verb  |  resource_attributes_verb  |   |  | |  Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "*" means all.  |
| spec_resource_attributes_version  |  resource_attributes_version  |   |  | |  Version is the API Version of the Resource. "*" means all.  |
| spec_user  |  user  |   |  | |  User is the user you're testing for. If you specify "User" but not "Group", then is it interpreted as "What if User were not a member of any groups  |
| ssl_ca_cert  |  |   |  | |  Path to a CA certificate used to authenticate with the API.  |
| username  |  |   |  | |  Provide a username for connecting to the API.  |
| verify_ssl  |  |   |  | |  Whether or not to verify the API server's SSL certificates.  |









#### Return

```yaml

api_version:
  type: string
  description: Requested API version
subject_access_review:
  type: complex
  returned: on success
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
      description: []
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
      - Spec holds information about the request being evaluated
      type: complex
      contains:
        extra:
          description:
          - Extra corresponds to the user.Info.GetExtra() method from the authenticator.
            Since that is input to the authorizer it needs a reflection here.
          type: complex
          contains: str, list[str]
        group:
          description:
          - Groups is the groups you're testing for.
          type: list
          contains: str
        non_resource_attributes:
          description:
          - NonResourceAttributes describes information for a non-resource access
            request
          type: complex
          contains:
            path:
              description:
              - Path is the URL path of the request
              type: str
            verb:
              description:
              - Verb is the standard HTTP verb
              type: str
        resource_attributes:
          description:
          - ResourceAuthorizationAttributes describes information for a resource access
            request
          type: complex
          contains:
            group:
              description:
              - Group is the API Group of the Resource. "*" means all.
              type: str
            name:
              description:
              - Name is the name of the resource being requested for a "get" or deleted
                for a "delete". "" (empty) means all.
              type: str
            namespace:
              description:
              - Namespace is the namespace of the action being requested. Currently,
                there is no distinction between no namespace and all namespaces ""
                (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty
                for cluster-scoped resources "" (empty) means "all" for namespace
                scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
              type: str
            resource:
              description:
              - Resource is one of the existing resource types. "*" means all.
              type: str
            subresource:
              description:
              - Subresource is one of the existing resource types. "" means none.
              type: str
            verb:
              description:
              - 'Verb is a kubernetes resource API verb, like: get, list, watch, create,
                update, delete, proxy. "*" means all.'
              type: str
            version:
              description:
              - Version is the API Version of the Resource. "*" means all.
              type: str
        user:
          description:
          - User is the user you're testing for. If you specify "User" but not "Group",
            then is it interpreted as "What if User were not a member of any groups
          type: str
    status:
      description:
      - Status is filled in by the server and indicates whether the request is allowed
        or not
      type: complex
      contains:
        allowed:
          description:
          - Allowed is required. True if the action would be allowed, false otherwise.
          type: bool
        evaluation_error:
          description:
          - EvaluationError is an indication that some error occurred during the authorization
            check. It is entirely possible to get an error and be able to continue
            determine authorization status in spite of it. For instance, RBAC can
            be missing a role, but enough roles are still present and bound to reason
            about the request.
          type: str
        reason:
          description:
          - Reason is optional. It indicates why a request was allowed or denied.
          type: str

```





---