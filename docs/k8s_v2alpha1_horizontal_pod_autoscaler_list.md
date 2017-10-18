
## k8s_v2alpha1_horizontal_pod_autoscaler_list

Kubernetes HorizontalPodAutoscalerList

Author: OpenShift (@openshift)

Version added: 2.3.0





---
### Requirements

* kubernetes == 3.0.0




---

  * [Synopsis](#Synopsis)

  * [Options](#Options)


* [Return](#Return)



#### Synopsis
Retrieve a list of horizontal_pod_autoscalers. List operations provide a snapshot read of the underlying objects, returning a resource_version representing a consistent version of the listed objects.


#### Options

| Parameter     |  aliases     | required    | default  | choices    | comments |
| ------------- |------------- |-------------| ---------|----------- |--------- |
| api_key  |  |   |  | |  Token used to connect to the API.  |
| cert_file  |  |   |  | |  Path to a certificate used to authenticate with the API.  |
| context  |  |   |  | |  The name of a context found in the Kubernetes config file.  |
| debug  |  |   |  False  | |  Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log  |
| force  |  |   |  False  | |  If set to C(True), and I(state) is C(present), an existing object will updated, and lists will be replaced, rather than merged.  |
| host  |  |   |  | |  Provide a URL for acessing the Kubernetes API.  |
| key_file  |  |   |  | |  Path to a key file used to authenticate with the API.  |
| kubeconfig  |  |   |  | |  Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json).  |
| password  |  |   |  | |  Provide a password for connecting to the API. Use in conjunction with I(username).  |
| resource_definition  |  |   |  | |  Provide the YAML definition for the object, bypassing any modules parameters intended to define object attributes.  |
| src  |  |   |  | |  Provide a path to a file containing the YAML definition of the object. Mutually exclusive with I(resource_definition).  |
| ssl_ca_cert  |  |   |  | |  Path to a CA certificate used to authenticate with the API.  |
| state  |  |   |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Determines if an object should be created, patched, or deleted. When set to C(present), the object will be created, if it does not exist, or patched, if parameter values differ from the existing object's attributes, and deleted, if set to C(absent). A patch operation results in merging lists and updating dictionaries, with lists being merged into a unique set of values. If a list contains a dictionary with a I(name) or I(type) attribute, a strategic merge is performed, where individual elements with a matching I(name_) or I(type) are merged. To force the replacement of lists, set the I(force) option to C(True).  |
| username  |  |   |  | |  Provide a username for connecting to the API.  |
| verify_ssl  |  |   |  | |  Whether or not to verify the API server's SSL certificates.  |









#### Return

```yaml

api_version:
  type: string
  description: Requested API version
horizontal_pod_autoscaler_list:
  type: complex
  returned: when I(state) = C(present)
  contains:
    api_version:
      description:
      - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values.
      type: str
    items:
      description:
      - items is the list of horizontal pod autoscaler objects.
      type: list
      contains:
        api_version:
          description:
          - APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value,
            and may reject unrecognized values.
          type: str
        kind:
          description:
          - Kind is a string value representing the REST resource this object represents.
            Servers may infer this from the endpoint the client submits requests to.
            Cannot be updated. In CamelCase.
          type: str
        metadata:
          description:
          - metadata is the standard object metadata.
          type: complex
          contains:
            annotations:
              description:
              - Annotations is an unstructured key value map stored with a resource
                that may be set by external tools to store and retrieve arbitrary
                metadata. They are not queryable and should be preserved when modifying
                objects.
              type: complex
              contains: str, str
            cluster_name:
              description:
              - The name of the cluster which the object belongs to. This is used
                to distinguish resources with same name and namespace in different
                clusters. This field is not set anywhere right now and apiserver is
                going to ignore it if set in create or update request.
              type: str
            creation_timestamp:
              description:
              - CreationTimestamp is a timestamp representing the server time when
                this object was created. It is not guaranteed to be set in happens-before
                order across separate operations. Clients may not set this value.
                It is represented in RFC3339 form and is in UTC. Populated by the
                system. Read-only. Null for lists.
              type: complex
              contains: {}
            deletion_grace_period_seconds:
              description:
              - Number of seconds allowed for this object to gracefully terminate
                before it will be removed from the system. Only set when deletionTimestamp
                is also set. May only be shortened. Read-only.
              type: int
            deletion_timestamp:
              description:
              - DeletionTimestamp is RFC 3339 date and time at which this resource
                will be deleted. This field is set by the server when a graceful deletion
                is requested by the user, and is not directly settable by a client.
                The resource is expected to be deleted (no longer visible from resource
                lists, and not reachable by name) after the time in this field. Once
                set, this value may not be unset or be set further into the future,
                although it may be shortened or the resource may be deleted prior
                to this time. For example, a user may request that a pod is deleted
                in 30 seconds. The Kubelet will react by sending a graceful termination
                signal to the containers in the pod. After that 30 seconds, the Kubelet
                will send a hard termination signal (SIGKILL) to the container and
                after cleanup, remove the pod from the API. In the presence of network
                partitions, this object may still exist after this timestamp, until
                an administrator or automated process can determine the resource is
                fully terminated. If not set, graceful deletion of the object has
                not been requested. Populated by the system when a graceful deletion
                is requested. Read-only.
              type: complex
              contains: {}
            finalizers:
              description:
              - Must be empty before the object is deleted from the registry. Each
                entry is an identifier for the responsible component that will remove
                the entry from the list. If the deletionTimestamp of the object is
                non-nil, entries in this list can only be removed.
              type: list
              contains: str
            generate_name:
              description:
              - GenerateName is an optional prefix, used by the server, to generate
                a unique name ONLY IF the Name field has not been provided. If this
                field is used, the name returned to the client will be different than
                the name passed. This value will also be combined with a unique suffix.
                The provided value has the same validation rules as the Name field,
                and may be truncated by the length of the suffix required to make
                the value unique on the server. If this field is specified and the
                generated name exists, the server will NOT return a 409 - instead,
                it will either return 201 Created or 500 with Reason ServerTimeout
                indicating a unique name could not be found in the time allotted,
                and the client should retry (optionally after the time indicated in
                the Retry-After header). Applied only if Name is not specified.
              type: str
            generation:
              description:
              - A sequence number representing a specific generation of the desired
                state. Populated by the system. Read-only.
              type: int
            initializers:
              description:
              - An initializer is a controller which enforces some system invariant
                at object creation time. This field is a list of initializers that
                have not yet acted on this object. If nil or empty, this object has
                been completely initialized. Otherwise, the object is considered uninitialized
                and is hidden (in list/watch and get calls) from clients that haven't
                explicitly asked to observe uninitialized objects. When an object
                is created, the system will populate this list with the current set
                of initializers. Only privileged users may set or modify this list.
                Once it is empty, it may not be modified further by any user.
              type: complex
              contains:
                pending:
                  description:
                  - Pending is a list of initializers that must execute in order before
                    this object is visible. When the last pending initializer is removed,
                    and no failing result is set, the initializers struct will be
                    set to nil and the object is considered as initialized and visible
                    to all clients.
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
                        of an object. Servers should convert recognized schemas to
                        the latest internal value, and may reject unrecognized values.
                      type: str
                    code:
                      description:
                      - Suggested HTTP return code for this status, 0 if not set.
                      type: int
                    details:
                      description:
                      - Extended data associated with the reason. Each reason may
                        define its own extended details. This field is optional and
                        the data returned is not guaranteed to conform to any schema
                        except that defined by the reason type.
                      type: complex
                      contains:
                        causes:
                          description:
                          - The Causes array includes more details associated with
                            the StatusReason failure. Not all StatusReasons may provide
                            detailed causes.
                          type: list
                          contains:
                            field:
                              description:
                              - 'The field of the resource that has caused this error,
                                as named by its JSON serialization. May include dot
                                and postfix notation for nested attributes. Arrays
                                are zero-indexed. Fields may appear more than once
                                in an array of causes due to fields having multiple
                                errors. Optional. Examples: "name" - the field "name"
                                on the current resource "items[0].name" - the field
                                "name" on the first array entry in "items"'
                              type: str
                            message:
                              description:
                              - A human-readable description of the cause of the error.
                                This field may be presented as-is to a reader.
                              type: str
                            reason:
                              description:
                              - A machine-readable description of the cause of the
                                error. If this value is empty there is no information
                                available.
                              type: str
                        group:
                          description:
                          - The group attribute of the resource associated with the
                            status StatusReason.
                          type: str
                        kind:
                          description:
                          - The kind attribute of the resource associated with the
                            status StatusReason. On some operations may differ from
                            the requested resource Kind.
                          type: str
                        name:
                          description:
                          - The name attribute of the resource associated with the
                            status StatusReason (when there is a single name which
                            can be described).
                          type: str
                        retry_after_seconds:
                          description:
                          - If specified, the time in seconds before the operation
                            should be retried.
                          type: int
                        uid:
                          description:
                          - UID of the resource. (when there is a single resource
                            which can be described).
                          type: str
                    kind:
                      description:
                      - Kind is a string value representing the REST resource this
                        object represents. Servers may infer this from the endpoint
                        the client submits requests to. Cannot be updated. In CamelCase.
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
                          - String that identifies the server's internal version of
                            this object that can be used by clients to determine when
                            objects have changed. Value must be treated as opaque
                            by clients and passed unmodified back to the server. Populated
                            by the system. Read-only.
                          type: str
                        self_link:
                          description:
                          - SelfLink is a URL representing this object. Populated
                            by the system. Read-only.
                          type: str
                    reason:
                      description:
                      - A machine-readable description of why this operation is in
                        the "Failure" status. If this value is empty there is no information
                        available. A Reason clarifies an HTTP status code but does
                        not override it.
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
              - Name must be unique within a namespace. Is required when creating
                resources, although some resources may allow a client to request the
                generation of an appropriate name automatically. Name is primarily
                intended for creation idempotence and configuration definition. Cannot
                be updated.
              type: str
            namespace:
              description:
              - Namespace defines the space within each name must be unique. An empty
                namespace is equivalent to the "default" namespace, but "default"
                is the canonical representation. Not all objects are required to be
                scoped to a namespace - the value of this field for those objects
                will be empty. Must be a DNS_LABEL. Cannot be updated.
              type: str
            owner_references:
              description:
              - List of objects depended by this object. If ALL objects in the list
                have been deleted, this object will be garbage collected. If this
                object is managed by a controller, then an entry in this list will
                point to this controller, with the controller field set to true. There
                cannot be more than one managing controller.
              type: list
              contains:
                api_version:
                  description:
                  - API version of the referent.
                  type: str
                block_owner_deletion:
                  description:
                  - If true, AND if the owner has the "foregroundDeletion" finalizer,
                    then the owner cannot be deleted from the key-value store until
                    this reference is removed. Defaults to false. To set this field,
                    a user needs "delete" permission of the owner, otherwise 422 (Unprocessable
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
              - An opaque value that represents the internal version of this object
                that can be used by clients to determine when objects have changed.
                May be used for optimistic concurrency, change detection, and the
                watch operation on a resource or set of resources. Clients must treat
                these values as opaque and passed unmodified back to the server. They
                may only be valid for a particular resource or set of resources. Populated
                by the system. Read-only. Value must be treated as opaque by clients
                and .
              type: str
            self_link:
              description:
              - SelfLink is a URL representing this object. Populated by the system.
                Read-only.
              type: str
            uid:
              description:
              - UID is the unique in time and space value for this object. It is typically
                generated by the server on successful creation of a resource and is
                not allowed to change on PUT operations. Populated by the system.
                Read-only.
              type: str
        spec:
          description:
          - spec is the specification for the behaviour of the autoscaler.
          type: complex
          contains:
            max_replicas:
              description:
              - maxReplicas is the upper limit for the number of replicas to which
                the autoscaler can scale up. It cannot be less that minReplicas.
              type: int
            metrics:
              description:
              - metrics contains the specifications for which to use to calculate
                the desired replica count (the maximum replica count across all metrics
                will be used). The desired replica count is calculated multiplying
                the ratio between the target value and the current value by the current
                number of pods. Ergo, metrics used must decrease as the pod count
                is increased, and vice-versa. See the individual metric source types
                for more information about how each type of metric must respond.
              type: list
              contains:
                object:
                  description:
                  - object refers to a metric describing a single kubernetes object
                    (for example, hits-per-second on an Ingress object).
                  type: complex
                  contains:
                    metric_name:
                      description:
                      - metricName is the name of the metric in question.
                      type: str
                    target:
                      description:
                      - target is the described Kubernetes object.
                      type: complex
                      contains:
                        api_version:
                          description:
                          - API version of the referent
                          type: str
                        kind:
                          description:
                          - Kind of the referent;
                          type: str
                        name:
                          description:
                          - Name of the referent;
                          type: str
                    target_value:
                      description:
                      - targetValue is the target value of the metric (as a quantity).
                      type: str
                pods:
                  description:
                  - pods refers to a metric describing each pod in the current scale
                    target (for example, transactions-processed-per-second). The values
                    will be averaged together before being compared to the target
                    value.
                  type: complex
                  contains:
                    metric_name:
                      description:
                      - metricName is the name of the metric in question
                      type: str
                    target_average_value:
                      description:
                      - targetAverageValue is the target value of the average of the
                        metric across all relevant pods (as a quantity)
                      type: str
                resource:
                  description:
                  - resource refers to a resource metric (such as those specified
                    in requests and limits) known to Kubernetes describing each pod
                    in the current scale target (e.g. CPU or memory). Such metrics
                    are built in to Kubernetes, and have special scaling options on
                    top of those available to normal per-pod metrics using the "pods"
                    source.
                  type: complex
                  contains:
                    name:
                      description:
                      - name is the name of the resource in question.
                      type: str
                    target_average_utilization:
                      description:
                      - targetAverageUtilization is the target value of the average
                        of the resource metric across all relevant pods, represented
                        as a percentage of the requested value of the resource for
                        the pods.
                      type: int
                    target_average_value:
                      description:
                      - targetAverageValue is the target value of the average of the
                        resource metric across all relevant pods, as a raw value (instead
                        of as a percentage of the request), similar to the "pods"
                        metric source type.
                      type: str
                type:
                  description:
                  - type is the type of metric source. It should match one of the
                    fields below.
                  type: str
            min_replicas:
              description:
              - minReplicas is the lower limit for the number of replicas to which
                the autoscaler can scale down. It defaults to 1 pod.
              type: int
            scale_target_ref:
              description:
              - scaleTargetRef points to the target resource to scale, and is used
                to the pods for which metrics should be collected, as well as to actually
                change the replica count.
              type: complex
              contains:
                api_version:
                  description:
                  - API version of the referent
                  type: str
                kind:
                  description:
                  - Kind of the referent;
                  type: str
                name:
                  description:
                  - Name of the referent;
                  type: str
        status:
          description:
          - status is the current information about the autoscaler.
          type: complex
          contains:
            conditions:
              description:
              - conditions is the set of conditions required for this autoscaler to
                scale its target, and indicates whether or not those conditions are
                met.
              type: list
              contains:
                last_transition_time:
                  description:
                  - lastTransitionTime is the last time the condition transitioned
                    from one status to another
                  type: complex
                  contains: {}
                message:
                  description:
                  - message is a human-readable explanation containing details about
                    the transition
                  type: str
                reason:
                  description:
                  - reason is the reason for the condition's last transition.
                  type: str
                status:
                  description:
                  - status is the status of the condition (True, False, Unknown)
                  type: str
                type:
                  description:
                  - type describes the current condition
                  type: str
            current_metrics:
              description:
              - currentMetrics is the last read state of the metrics used by this
                autoscaler.
              type: list
              contains:
                object:
                  description:
                  - object refers to a metric describing a single kubernetes object
                    (for example, hits-per-second on an Ingress object).
                  type: complex
                  contains:
                    current_value:
                      description:
                      - currentValue is the current value of the metric (as a quantity).
                      type: str
                    metric_name:
                      description:
                      - metricName is the name of the metric in question.
                      type: str
                    target:
                      description:
                      - target is the described Kubernetes object.
                      type: complex
                      contains:
                        api_version:
                          description:
                          - API version of the referent
                          type: str
                        kind:
                          description:
                          - Kind of the referent;
                          type: str
                        name:
                          description:
                          - Name of the referent;
                          type: str
                pods:
                  description:
                  - pods refers to a metric describing each pod in the current scale
                    target (for example, transactions-processed-per-second). The values
                    will be averaged together before being compared to the target
                    value.
                  type: complex
                  contains:
                    current_average_value:
                      description:
                      - currentAverageValue is the current value of the average of
                        the metric across all relevant pods (as a quantity)
                      type: str
                    metric_name:
                      description:
                      - metricName is the name of the metric in question
                      type: str
                resource:
                  description:
                  - resource refers to a resource metric (such as those specified
                    in requests and limits) known to Kubernetes describing each pod
                    in the current scale target (e.g. CPU or memory). Such metrics
                    are built in to Kubernetes, and have special scaling options on
                    top of those available to normal per-pod metrics using the "pods"
                    source.
                  type: complex
                  contains:
                    current_average_utilization:
                      description:
                      - currentAverageUtilization is the current value of the average
                        of the resource metric across all relevant pods, represented
                        as a percentage of the requested value of the resource for
                        the pods. It will only be present if `targetAverageValue`
                        was set in the corresponding metric specification.
                      type: int
                    current_average_value:
                      description:
                      - currentAverageValue is the current value of the average of
                        the resource metric across all relevant pods, as a raw value
                        (instead of as a percentage of the request), similar to the
                        "pods" metric source type. It will always be set, regardless
                        of the corresponding metric specification.
                      type: str
                    name:
                      description:
                      - name is the name of the resource in question.
                      type: str
                type:
                  description:
                  - type is the type of metric source. It will match one of the fields
                    below.
                  type: str
            current_replicas:
              description:
              - currentReplicas is current number of replicas of pods managed by this
                autoscaler, as last seen by the autoscaler.
              type: int
            desired_replicas:
              description:
              - desiredReplicas is the desired number of replicas of pods managed
                by this autoscaler, as last calculated by the autoscaler.
              type: int
            last_scale_time:
              description:
              - lastScaleTime is the last time the HorizontalPodAutoscaler scaled
                the number of pods, used by the autoscaler to control how often the
                number of pods is changed.
              type: complex
              contains: {}
            observed_generation:
              description:
              - observedGeneration is the most recent generation observed by this
                autoscaler.
              type: int
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
      type: str
    metadata:
      description:
      - metadata is the standard list metadata.
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

```





---