# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from dialogflow_v2.proto import (
    context_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ContextsStub(object):
    """A context represents additional information included with user input or with
  an intent returned by the Dialogflow API. Contexts are helpful for
  differentiating user input which may be vague or have a different meaning
  depending on additional details from your application such as user setting
  and preferences, previous user input, where the user is in your application,
  geographic location, and so on.

  You can include contexts as input parameters of a
  [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
  [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) request,
  or as output contexts included in the returned intent.
  Contexts expire when an intent is matched, after the number of `DetectIntent`
  requests specified by the `lifespan_count` parameter, or after 20 minutes
  if no intents are matched for a `DetectIntent` request.

  For more information about contexts, see the
  [Dialogflow
  documentation](https://cloud.google.com/dialogflow-enterprise/docs/contexts-overview).
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.ListContexts = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Contexts/ListContexts",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.ListContextsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.ListContextsResponse.FromString,
        )
        self.GetContext = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Contexts/GetContext",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.GetContextRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.Context.FromString,
        )
        self.CreateContext = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Contexts/CreateContext",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.CreateContextRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.Context.FromString,
        )
        self.UpdateContext = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Contexts/UpdateContext",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.UpdateContextRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.Context.FromString,
        )
        self.DeleteContext = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Contexts/DeleteContext",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.DeleteContextRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.DeleteAllContexts = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Contexts/DeleteAllContexts",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.DeleteAllContextsRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ContextsServicer(object):
    """A context represents additional information included with user input or with
  an intent returned by the Dialogflow API. Contexts are helpful for
  differentiating user input which may be vague or have a different meaning
  depending on additional details from your application such as user setting
  and preferences, previous user input, where the user is in your application,
  geographic location, and so on.

  You can include contexts as input parameters of a
  [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
  [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) request,
  or as output contexts included in the returned intent.
  Contexts expire when an intent is matched, after the number of `DetectIntent`
  requests specified by the `lifespan_count` parameter, or after 20 minutes
  if no intents are matched for a `DetectIntent` request.

  For more information about contexts, see the
  [Dialogflow
  documentation](https://cloud.google.com/dialogflow-enterprise/docs/contexts-overview).
  """

    def ListContexts(self, request, context):
        """Returns the list of all contexts in the specified session.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetContext(self, request, context):
        """Retrieves the specified context.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateContext(self, request, context):
        """Creates a context.

    If the specified context already exists, overrides the context.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateContext(self, request, context):
        """Updates the specified context.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteContext(self, request, context):
        """Deletes the specified context.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteAllContexts(self, request, context):
        """Deletes all active contexts in the specified session.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ContextsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListContexts": grpc.unary_unary_rpc_method_handler(
            servicer.ListContexts,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.ListContextsRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.ListContextsResponse.SerializeToString,
        ),
        "GetContext": grpc.unary_unary_rpc_method_handler(
            servicer.GetContext,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.GetContextRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.Context.SerializeToString,
        ),
        "CreateContext": grpc.unary_unary_rpc_method_handler(
            servicer.CreateContext,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.CreateContextRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.Context.SerializeToString,
        ),
        "UpdateContext": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateContext,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.UpdateContextRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.Context.SerializeToString,
        ),
        "DeleteContext": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteContext,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.DeleteContextRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "DeleteAllContexts": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAllContexts,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.DeleteAllContextsRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.v2.Contexts", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
