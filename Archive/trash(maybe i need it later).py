with Container():
                                yield Select(()for Disk in GetNetworksInterfaces())
                                #@on(Select.Changed)
                                def select_changed(self, event: Select.Changed) -> None:
                                    if NetworkInterfaceStatus(event.value) == False:


                                            if NetworkInterfaceStatusOutput == "up":
                                                return(True)
                                            elif NetworkInterfaceStatusOutput == "down":
                                                return(False)
                                            else:
                                                return("Something went Wrong (Maybe your PC is Garbage)")


                                # WLAN Passwort
                                
                            def on_input_submitted(self, event: Input.Submitted) -> None:
                                value = event.value
                                self.query_one("#Password", input).value
                                if value == "wlan":

                                    subprocess.run(["iwctl"], ["station", value, "scan"])      