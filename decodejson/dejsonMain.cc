#include <iostream>
#include <fstream>
#include <string.h>
#include <memory>
#include "json/json.h"
#include "jsoncpp.cpp"

//https://github.com/open-source-parsers/jsoncpp

int main(int argc, char** argv){
    const char* document = "/home/prj2/symbolMaster.json";
    Json::CharReaderBuilder builder;
    Json::CharReader *reader = builder.newCharReader();

    std::ifstream is(document, std::ios::in);

    Json::Value root;
    JSONCPP_STRING errs;
    std::string lineFromDoc;
    while(std::getline(is, lineFromDoc)){
        if(reader->parse(lineFromDoc.c_str(), lineFromDoc.c_str() + lineFromDoc.size(), &root, &errs)){
            std::cout<<root["name"].asString()<<std::endl;
        }else{
            std::cout<<"Decode json failed!"<<std::endl;
        }
    }
//    }else{
//        std::cout<<"Decode Doc "<< document <<" failed"<<std::endl;
//    }

    is.close();
}
