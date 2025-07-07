# pip install pyusb
import usb.core
import usb.util

def list_usb_devices():
    devices = usb.core.find(find_all=True)
    for device in devices:
        print(f"ID: {hex(device.idVendor)}:{hex(device.idProduct)}")
        print(f"Manufacturer: {usb.util.get_string(device, device.iManufacturer)}")
        print(f"Product: {usb.util.get_string(device, device.iProduct)}")
        print(f"Serial Number: {usb.util.get_string(device, device.iSerialNumber)}")
        print("-" * 40)

if __name__ == "__main__":
    list_usb_devices()