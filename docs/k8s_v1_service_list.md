
## k8s_v1_service_list

Kubernetes ServiceList

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
Retrieve a list of services. List operations provide a snapshot read of the underlying objects, returning a resource_version representing a consistent version of the listed objects.


#### Options

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |

| username  |   |  | |  Provide a username for connecting to the API.  |

| src  |   |  | |  Provide a path to a file containing the YAML definition of the object. Mutually exclusive with I(resource_definition).  |

| api_key  |   |  | |  Token used to connect to the API.  |

| force  |   |  False  | |  If set to C(True), and I(state) is C(present), an existing object will updated, and lists will be replaced, rather than merged.  |

| ssl_ca_cert  |   |  | |  Path to a CA certificate used to authenticate with the API.  |

| cert_file  |   |  | |  Path to a certificate used to authenticate with the API.  |

| state  |   |  present  |  - present  - absent  |  Determines if an object should be created, patched, or deleted. When set to C(present), the object will be created, if it does not exist, or patched, if parameter values differ from the existing object's attributes, and deleted, if set to C(absent). A patch operation results in merging lists and updating dictionaries, with lists being merged into a unique set of values. If a list contains a dictionary with a I(name) or I(type) attribute, a strategic merge is performed, where individual elements with a matching I(name_) or I(type) are merged. To force the replacement of lists, set the I(force) option to C(True).  |

| kubeconfig  |   |  | |  Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json).  |

| debug  |   |  False  | |  Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log  |

| verify_ssl  |   |  | |  Whether or not to verify the API server's SSL certificates.  |

| context  |   |  | |  The name of a context found in the Kubernetes config file.  |

| host  |   |  | |  Provide a URL for acessing the Kubernetes API.  |

| resource_definition  |   |  | |  Provide the YAML definition for the object, bypassing any modules parameters intended to define object attributes.  |

| key_file  |   |  | |  Path to a key file used to authenticate with the API.  |

| password  |   |  | |  Provide a password for connecting to the API. Use in conjunction with I(username).  |







#### Examples

```





```




#### Return

```yaml

api_version:
  type: string
  description: Requested API version
service_list:
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
      - List of services
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
          - Standard object's metadata.
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
          - Spec defines the behavior of a service.
          type: complex
          contains:
            cluster_ip:
              description:
              - clusterIP is the IP address of the service and is usually assigned
                randomly by the master. If an address is specified manually and is
                not in use by others, it will be allocated to the service; otherwise,
                creation of the service will fail. This field can not be changed through
                updates. Valid values are "None", empty string (""), or a valid IP
                address. "None" can be specified for headless services when proxying
                is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer.
                Ignored if type is ExternalName.
              type: str
            external_i_ps:
              description:
              - externalIPs is a list of IP addresses for which nodes in the cluster
                will also accept traffic for this service. These IPs are not managed
                by Kubernetes. The user is responsible for ensuring that traffic arrives
                at a node with this IP. A common example is external load-balancers
                that are not part of the Kubernetes system.
              type: list
              contains: str
            external_name:
              description:
              - externalName is the external reference that kubedns or equivalent
                will return as a CNAME record for this service. No proxying will be
                involved. Must be a valid DNS name and requires Type to be ExternalName.
              type: str
            external_traffic_policy:
              description:
              - externalTrafficPolicy denotes if this Service desires to route external
                traffic to node-local or cluster-wide endpoints. "Local" preserves
                the client source IP and avoids a second hop for LoadBalancer and
                Nodeport type services, but risks potentially imbalanced traffic spreading.
                "Cluster" obscures the client source IP and may cause a second hop
                to another node, but should have good overall load-spreading.
              type: str
            health_check_node_port:
              description:
              - healthCheckNodePort specifies the healthcheck nodePort for the service.
                If not specified, HealthCheckNodePort is created by the service api
                backend with the allocated nodePort. Will use user-specified nodePort
                value if specified by the client. Only effects when Type is set to
                LoadBalancer and ExternalTrafficPolicy is set to Local.
              type: int
            load_balancer_ip:
              description:
              - 'Only applies to Service Type: LoadBalancer LoadBalancer will get
                created with the IP specified in this field. This feature depends
                on whether the underlying cloud-provider supports specifying the loadBalancerIP
                when a load balancer is created. This field will be ignored if the
                cloud-provider does not support the feature.'
              type: str
            load_balancer_source_ranges:
              description:
              - If specified and supported by the platform, this will restrict traffic
                through the cloud-provider load-balancer will be restricted to the
                specified client IPs. This field will be ignored if the cloud-provider
                does not support the feature."
              type: list
              contains: str
            ports:
              description:
              - The list of ports that are exposed by this service.
              type: list
              contains:
                name:
                  description:
                  - The name of this port within the service. This must be a DNS_LABEL.
                    All ports within a ServiceSpec must have unique names. This maps
                    to the 'Name' field in EndpointPort objects. Optional if only
                    one ServicePort is defined on this service.
                  type: str
                node_port:
                  description:
                  - The port on each node on which this service is exposed when type=NodePort
                    or LoadBalancer. Usually assigned by the system. If specified,
                    it will be allocated to the service if unused or else creation
                    of the service will fail. Default is to auto-allocate a port if
                    the ServiceType of this Service requires one.
                  type: int
                port:
                  description:
                  - The port that will be exposed by this service.
                  type: int
                protocol:
                  description:
                  - The IP protocol for this port. Supports "TCP" and "UDP". Default
                    is TCP.
                  type: str
                target_port:
                  description:
                  - Number or name of the port to access on the pods targeted by the
                    service. Number must be in the range 1 to 65535. Name must be
                    an IANA_SVC_NAME. If this is a string, it will be looked up as
                    a named port in the target Pod's container ports. If this is not
                    specified, the value of the 'port' field is used (an identity
                    map). This field is ignored for services with clusterIP=None,
                    and should be omitted or set equal to the 'port' field.
                  type: str
            selector:
              description:
              - Route service traffic to pods with label keys and values matching
                this selector. If empty or not present, the service is assumed to
                have an external process managing its endpoints, which Kubernetes
                will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer.
                Ignored if type is ExternalName.
              type: complex
              contains: str, str
            session_affinity:
              description:
              - Supports "ClientIP" and "None". Used to maintain session affinity.
                Enable client IP based session affinity. Must be ClientIP or None.
                Defaults to None.
              type: str
            type:
              description:
              - type determines how the Service is exposed. Defaults to ClusterIP.
                Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer.
                "ExternalName" maps to the specified externalName. "ClusterIP" allocates
                a cluster-internal IP address for load-balancing to endpoints. Endpoints
                are determined by the selector or if that is not specified, by manual
                construction of an Endpoints object. If clusterIP is "None", no virtual
                IP is allocated and the endpoints are published as a set of endpoints
                rather than a stable IP. "NodePort" builds on ClusterIP and allocates
                a port on every node which routes to the clusterIP. "LoadBalancer"
                builds on NodePort and creates an external load-balancer (if supported
                in the current cloud) which routes to the clusterIP.
              type: str
        status:
          description:
          - Most recently observed status of the service. Populated by the system.
            Read-only.
          type: complex
          contains:
            load_balancer:
              description:
              - LoadBalancer contains the current status of the load-balancer, if
                one is present.
              type: complex
              contains:
                ingress:
                  description:
                  - Ingress is a list containing ingress points for the load-balancer.
                    Traffic intended for the service should be sent to these ingress
                    points.
                  type: list
                  contains:
                    hostname:
                      description:
                      - Hostname is set for load-balancer ingress points that are
                        DNS based (typically AWS load-balancers)
                      type: str
                    ip:
                      description:
                      - IP is set for load-balancer ingress points that are IP based
                        (typically GCE or OpenStack load-balancers)
                      type: str
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
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

```





---