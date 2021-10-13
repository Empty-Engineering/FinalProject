#include <iostream>
std::string encrypt(std::string msg, std::string key="f6952d6eef555ddd87aca66e56b91530222d6e318414816f3ba7cf5bf694bf0f"){
    std::string tmp(key);
    while (key.size() < msg.size())
        key += tmp;
    for (std::string::size_type i = 0; i < msg.size(); ++i)
        msg[i] ^= key[i];
    return msg;
}
const char* get_hash(const char* message){
    std::string hash = encrypt(message);
    const char* hash_final = hash.c_str();
    return hash_final;
}
