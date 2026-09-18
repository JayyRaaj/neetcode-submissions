class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = [s.encode('utf-8') for s in strs]
        return encoded_list


    def decode(self, s: str) -> List[str]:
        decoded_list = [s.decode('utf-8') for s in s]
        return decoded_list

