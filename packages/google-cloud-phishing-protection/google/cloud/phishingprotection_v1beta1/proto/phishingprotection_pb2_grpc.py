# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.phishingprotection_v1beta1.proto import (
    phishingprotection_pb2 as google_dot_cloud_dot_phishingprotection__v1beta1_dot_proto_dot_phishingprotection__pb2,
)


class PhishingProtectionServiceV1Beta1Stub(object):
    """Service to report phishing URIs.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.ReportPhishing = channel.unary_unary(
            "/google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1/ReportPhishing",
            request_serializer=google_dot_cloud_dot_phishingprotection__v1beta1_dot_proto_dot_phishingprotection__pb2.ReportPhishingRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_phishingprotection__v1beta1_dot_proto_dot_phishingprotection__pb2.ReportPhishingResponse.FromString,
        )


class PhishingProtectionServiceV1Beta1Servicer(object):
    """Service to report phishing URIs.
  """

    def ReportPhishing(self, request, context):
        """Reports a URI suspected of containing phishing content to be reviewed. Once
    the report review is completed, if its result verifies the existince of
    malicious phishing content, the site will be added the to [Google's Social
    Engineering lists](https://support.google.com/webmasters/answer/6350487/)
    in order to protect users that could get exposed to this threat in
    the future.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PhishingProtectionServiceV1Beta1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ReportPhishing": grpc.unary_unary_rpc_method_handler(
            servicer.ReportPhishing,
            request_deserializer=google_dot_cloud_dot_phishingprotection__v1beta1_dot_proto_dot_phishingprotection__pb2.ReportPhishingRequest.FromString,
            response_serializer=google_dot_cloud_dot_phishingprotection__v1beta1_dot_proto_dot_phishingprotection__pb2.ReportPhishingResponse.SerializeToString,
        )
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))
