# def routing(config, window):
#     try:
#         with telnetlib.Telnet(config['IP']) as telnet:
#             telnet.read_until(b"Username")
#             telnet.write(to_bytes(config['Username']))
#             telnet.read_until(b"Password")
#             telnet.write(to_bytes(config['Password']))
#             index, m, output = telnet.expect([b">", b"#"])
#             if index == 0:
#                 telnet.write(b"enable\n")
#                 telnet.read_until(b"Password")
#                 telnet.write(to_bytes(config['Enable']))
#                 telnet.read_until(b"#", timeout=5)
#             telnet.write(b"terminal length 0\n")
#             telnet.read_until(b"#", timeout=5)
#             time.sleep(3)
#             telnet.read_very_eager()

#             result = {}
#             commands = typeconfig(config)
#             for command in commands:
#                 telnet.write(to_bytes(command))
#                 output = telnet.read_until(b"#", timeout=5).decode("utf-8")
#                 result[command] = output.replace("\r\n", "\n")
#             telnet.write(to_bytes("show running-config"))
#             output = telnet.read_until(b"#", timeout=5).decode("utf-8")
#             result["show running-config"] = output.replace("\r\n", "\n")
#             pprint(result, width=120)
#             saveconfig(config)
#             return result
#     except TimeoutError as e:
#         messagebox.showerror("Error", e, parent=window)
