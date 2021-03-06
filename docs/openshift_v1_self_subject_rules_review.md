
## openshift_v1_self_subject_rules_review

OpenShift SelfSubjectRulesReview

Author: OpenShift (@openshift)

Version added: 2.3.0





---
### Requirements

* openshift == 0.3.3




---

  * [Synopsis](#synopsis)

  * [Options](#options)


* [Return](#return)



#### Synopsis
Manage the lifecycle of a self_subject_rules_review object. Supports check mode, and attempts to to be idempotent.


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
| spec_scopes  |  scopes  |   |  | |  Scopes to use for the evaluation. Empty means "use the unscoped (full) permissions of the user/groups". Nil means "use the scopes on this request".  |
| ssl_ca_cert  |  |   |  | |  Path to a CA certificate used to authenticate with the API.  |
| username  |  |   |  | |  Provide a username for connecting to the API.  |
| verify_ssl  |  |   |  | |  Whether or not to verify the API server's SSL certificates.  |









#### Return

```yaml

api_version:
  type: string
  description: Requested API version
self_subject_rules_review:
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
    spec:
      description:
      - Spec adds information about how to conduct the check
      type: complex
      contains:
        scopes:
          description:
          - Scopes to use for the evaluation. Empty means "use the unscoped (full)
            permissions of the user/groups". Nil means "use the scopes on this request".
          type: list
          contains: str
    status:
      description:
      - Status is completed by the server to tell which permissions you have
      type: complex
      contains:
        evaluation_error:
          description:
          - EvaluationError can appear in combination with Rules. It means some error
            happened during evaluation that may have prevented additional rules from
            being populated.
          type: str
        rules:
          description:
          - Rules is the list of rules (no particular sort) that are allowed for the
            subject
          type: list
          contains:
            api_groups:
              description:
              - APIGroups is the name of the APIGroup that contains the resources.
                If this field is empty, then both kubernetes and origin API groups
                are assumed. That means that if an action is requested against one
                of the enumerated resources in either the kubernetes or the origin
                API group, the request will be allowed
              type: list
              contains: str
            attribute_restrictions:
              description:
              - AttributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder
                pair supports. If the Authorizer does not recognize how to handle
                the AttributeRestrictions, the Authorizer should report an error.
              type: complex
              contains:
                raw:
                  description:
                  - Raw is the underlying serialization of this object.
                  type: str
            non_resource_ur_ls:
              description:
              - NonResourceURLsSlice is a set of partial urls that a user should have
                access to. *s are allowed, but only as the full, final step in the
                path This name is intentionally different than the internal type so
                that the DefaultConvert works nicely and because the ordering may
                be different.
              type: list
              contains: str
            resource_names:
              description:
              - ResourceNames is an optional white list of names that the rule applies
                to. An empty set means that everything is allowed.
              type: list
              contains: str
            resources:
              description:
              - Resources is a list of resources this rule applies to. ResourceAll
                represents all resources.
              type: list
              contains: str
            verbs:
              description:
              - Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions
                contained in this rule. VerbAll represents all kinds.
              type: list
              contains: str

```





---