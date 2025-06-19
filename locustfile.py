


# from locust import User, task, between, events
# from websocket import create_connection, WebSocketConnectionClosedException, WebSocketTimeoutException
# import base64
# import time
# import random
#
# AUTH_TOKEN = "Bearer your_token_here"
#
# MOVE_MESSAGES_BASE64 = [
#     "Jm5vdGlmaWNhdGlvbjpjbWFuYnNkNHcwMDAzZTg2b3piaGp3aGxnAACOA0P2+MvtDyDIvq7IDwG59LKtD2bo8LiTDwWUpNOQDwGE55nbDhX+6PjTDhG8saSuDgG35OiYDgHHrprWDQGc4eeKDQHdj5aGDQH88svNDAGl3+TADAa09tC9DAGQzeSiDAGmgpOeDAP3osaJDAPn24LNCwHPxo2yCwX2pbiYCinwy7PiCQLX4JHBCQGP2eW/CQGqgM3LCF7G1dvJCBO7o/K+CAGN5d+5CAH4w43wBwHww/brByv6grfoBwHetNLeBwHB3LO2BwG66cemBwHJ3oSMBwHI4+zbBh3ezbOyBgGPl7usBgGBqaemBgH05IX1BRSou6XoBQHCs/LYBQWv8ZC+BRi5wNazBQHn/tOOBQH7+pmIBQH0/ufyBAGn1/PNBAH/4LK0BHbMkPGeBAHWrsr/Ax2wkL3ZAwHTgNSMAwHTxZPXAgXBn5jDAiqc14PBAgGKmKeQAgH+rJ+NAhiUzPz8AQHDgezyAQH17srRAQHFv8WiAQGmqthiAdvop14B1u6wUQSsjptAAc38xQsB",
#     "Jm5vdGlmaWNhdGlvbjpjbWFuYnNkNHcwMDAzZTg2b3piaGp3aGxnAQoBzfq9pQQAAnt9",
#     "Jm5vdGlmaWNhdGlvbjpjbWFuYnNkNHcwMDAzZTg2b3piaGp3aGxnASkEt/v68AyEBQJ7fdOf2M4F9gICe32j6dPoC/UDAnt9pP3DggasBAJ7fQ=="
# ]
#
# MOVE_MESSAGES = [base64.b64decode(msg) for msg in MOVE_MESSAGES_BASE64]
#
# class WebSocketUser(User):
#     wait_time = between(1, 1)
#
#     def on_start(self):
#         self.ws = None
#         try:
#             headers = {
#                 "Authorization": AUTH_TOKEN,
#                 "Origin": "https://dev.editorup.com",
#             }
#             self.ws = create_connection(
#                 "wss://api.editorup.com/api/v1/ws",
#                 header=[f"{key}: {value}" for key, value in headers.items()],
#                 timeout=5  # 设置超时时间，防止无限等待
#             )
#
#         except Exception as e:
#             events.request.fire(
#                 request_type="WebSocket",
#                 name="connect",
#                 response_time=0,
#                 response_length=0,
#                 exception=e,
#             )
#
#     def on_stop(self):
#         if self.ws:
#             try:
#                 self.ws.close()
#             except Exception:
#                 pass
#
#     @task
#     def move_layer(self):
#         if not self.ws:
#             return
#         message = random.choice(MOVE_MESSAGES)
#         try:
#             start_time = time.perf_counter()
#             self.ws.send(message, opcode=2)
#             # 等待服务器返回消息作为响应
#             response = self.ws.recv()  # 阻塞等待消息，或者可以设置超时
#             total_time = (time.perf_counter() - start_time) * 1000
#             events.request.fire(
#                 request_type="WebSocket",
#                 name="move_layer",
#                 response_time=total_time,
#                 response_length=len(response),
#                 exception=None,
#             )
#         except WebSocketTimeoutException as e:
#             # 超时可以视作失败
#             events.request.fire(
#                 request_type="WebSocket",
#                 name="move_layer",
#                 response_time=0,
#                 response_length=0,
#                 exception=e,
#             )
#         except WebSocketConnectionClosedException as e:
#             events.request.fire(
#                 request_type="WebSocket",
#                 name="move_layer",
#                 response_time=0,
#                 response_length=0,
#                 exception=e,
#             )
#             self.ws = None
#         except Exception as e:
#             events.request.fire(
#                 request_type="WebSocket",
#                 name="move_layer",
#                 response_time=0,
#                 response_length=0,
#                 exception=e,
#             )




from locust import User, task, between, events
from websocket import create_connection, WebSocketConnectionClosedException, WebSocketTimeoutException
import base64
import time

AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJjbWFuYnNkNHcwMDAzZTg2b3piaGp3aGxnIiwibmFtZSI6IjE4ODg4ODg4ODg4Iiwicm9sZSI6InZpcCIsImlhdCI6MTc0OTE5NzY5NywiZXhwIjoxNzQ5MjAxMjk3fQ.w95U4QUzwrwOBTbWAfoIV66ajaaWLqOECxLci_7owS8"

# 只使用你指定的 base64 消息
MOVE_MESSAGES_BASE64 = [
    "GWNtYmtocjUzeTAwMHFienFvM2R5dWVtYWoAAukCARCZ78LwBRAnAKP/87YIAB42ODQyYWI5N2ZURFlDZ2NkazRTbUptWHBWbVEyZ1UBKACZ78LwBRACaWQBdx42ODQyYWI5N2ZURFlDZ2NkazRTbUptWHBWbVEyZ1UoAJnvwvAFEARuYW1lAXcAKACZ78LwBRAGbG9ja2VkAXkoAJnvwvAFEAd2aXNpYmxlAXgnAJnvwvAFEApiYWNrZ3JvdW5kASgAme/C8AUVBmxvY2tlZAF5KACZ78LwBRUFY29sb3IBdwcjRkZGRkZGJwCZ78LwBRAEc2l6ZQEoAJnvwvAFGAV3aWR0aAF9gB4oAJnvwvAFGAZoZWlnaHQBfbgQJwCZ78LwBRAFdGhlbWUBJwCZ78LwBRsGY29sb3JzACcAme/C8AUQBm9yZGVycwAnAJnvwvAFEAhlbGVtZW50cwGIme/C8AUPAXceNjg0MmFiOTdmVERZQ2djZGs0U21KbVhwVm1RMmdVAA=="
    # "GWNtYmtocjUzeTAwMHFienFvM2R5dWVtYWoAAukCARDF4cbKDCInAKP/87YIAB42ODQyYTlmZmJSNnlZWE1YNzlDMmo3UnZTZG54VGsBKADF4cbKDCICaWQBdx42ODQyYTlmZmJSNnlZWE1YNzlDMmo3UnZTZG54VGsoAMXhxsoMIgRuYW1lAXcAKADF4cbKDCIGbG9ja2VkAXkoAMXhxsoMIgd2aXNpYmxlAXgnAMXhxsoMIgpiYWNrZ3JvdW5kASgAxeHGygwnBmxvY2tlZAF5KADF4cbKDCcFY29sb3IBdwcjRkZGRkZGJwDF4cbKDCIEc2l6ZQEoAMXhxsoMKgV3aWR0aAF9gB4oAMXhxsoMKgZoZWlnaHQBfbgQJwDF4cbKDCIFdGhlbWUBJwDF4cbKDC0GY29sb3JzACcAxeHGygwiBm9yZGVycwAnAMXhxsoMIghlbGVtZW50cwGIxeHGygwhAXceNjg0MmE5ZmZiUjZ5WVhNWDc5QzJqN1J2U2RueFRrAA=="
]

MOVE_MESSAGES = [base64.b64decode(msg) for msg in MOVE_MESSAGES_BASE64]

class WebSocketUser(User):
    wait_time = between(1, 1)

    def on_start(self):
        # page = {id: "cmbkkgzwv000wbzqodfi5g6w8"}
        self.ws = None
        try:
            headers = {
                "Authorization": AUTH_TOKEN,
                "Origin": "https://dev.editorup.com",
            }
            self.ws = create_connection(
                "wss://api.editorup.com/api/v1/ws",
                header=[f"{key}: {value}" for key, value in headers.items()],
                timeout=5
            )
        except Exception as e:
            events.request.fire(
                request_type="WebSocket",
                name="connect",
                response_time=0,
                response_length=0,
                exception=e,
            )

    def on_stop(self):
        if self.ws:
            try:
                self.ws.close()
            except Exception:
                pass

    @task
    def move_layer(self):
        if not self.ws:
            return
        message = MOVE_MESSAGES[0]
        try:
            start_time = time.perf_counter()
            self.ws.send(message, opcode=2)
            response = self.ws.recv()
            total_time = (time.perf_counter() - start_time) * 1000
            events.request.fire(
                request_type="WebSocket",
                name="move_layer",
                response_time=total_time,
                response_length=len(response),
                exception=None,
            )
        except WebSocketTimeoutException as e:
            events.request.fire(
                request_type="WebSocket",
                name="move_layer",
                response_time=0,
                response_length=0,
                exception=e,
            )
        except WebSocketConnectionClosedException as e:
            events.request.fire(
                request_type="WebSocket",
                name="move_layer",
                response_time=0,
                response_length=0,
                exception=e,
            )
            self.ws = None
        except Exception as e:
            events.request.fire(
                request_type="WebSocket",
                name="move_layer",
                response_time=0,
                response_length=0,
                exception=e,
            )




# GWNtYmtocjUzeTAwMHFienFvM2R5dWVtYWoAAukCARCZ78LwBQAnAKP/87YIAB42ODQyYWI4Mm5XOUhQZTJnV0I5N0N3c2FVdnludnABKACZ78LwBQACaWQBdx42ODQyYWI4Mm5XOUhQZTJnV0I5N0N3c2FVdnludnAoAJnvwvAFAARuYW1lAXcAKACZ78LwBQAGbG9ja2VkAXkoAJnvwvAFAAd2aXNpYmxlAXgnAJnvwvAFAApiYWNrZ3JvdW5kASgAme/C8AUFBmxvY2tlZAF5KACZ78LwBQUFY29sb3IBdwcjRkZGRkZGJwCZ78LwBQAEc2l6ZQEoAJnvwvAFCAV3aWR0aAF9gB4oAJnvwvAFCAZoZWlnaHQBfbgQJwCZ78LwBQAFdGhlbWUBJwCZ78LwBQsGY29sb3JzACcAme/C8AUABm9yZGVycwAnAJnvwvAFAAhlbGVtZW50cwGIm+qA7gsPAXceNjg0MmFiODJuVzlIUGUyZ1dCOTdDd3NhVXZ5bnZwAA==
# GWNtYmtocjUzeTAwMHFienFvM2R5dWVtYWoAAukCARCZ78LwBRAnAKP/87YIAB42ODQyYWI5N2ZURFlDZ2NkazRTbUptWHBWbVEyZ1UBKACZ78LwBRACaWQBdx42ODQyYWI5N2ZURFlDZ2NkazRTbUptWHBWbVEyZ1UoAJnvwvAFEARuYW1lAXcAKACZ78LwBRAGbG9ja2VkAXkoAJnvwvAFEAd2aXNpYmxlAXgnAJnvwvAFEApiYWNrZ3JvdW5kASgAme/C8AUVBmxvY2tlZAF5KACZ78LwBRUFY29sb3IBdwcjRkZGRkZGJwCZ78LwBRAEc2l6ZQEoAJnvwvAFGAV3aWR0aAF9gB4oAJnvwvAFGAZoZWlnaHQBfbgQJwCZ78LwBRAFdGhlbWUBJwCZ78LwBRsGY29sb3JzACcAme/C8AUQBm9yZGVycwAnAJnvwvAFEAhlbGVtZW50cwGIme/C8AUPAXceNjg0MmFiOTdmVERZQ2djZGs0U21KbVhwVm1RMmdVAA==