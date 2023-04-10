#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <chrono>
#include <thread>
#include <vector>
#include <windows.h>
#include <cstring>
#include <ctime>
#include <filesystem>

using namespace std;

void display_ascii_art(const string &filename, int &row, const string &color_code, int scroll_speed);
void random_ascii_art(const string &folder, string &filename);
int get_console_width();

string get_executable_path() {
    char buffer[MAX_PATH];
    GetModuleFileName(NULL, buffer, MAX_PATH);
    string::size_type pos = string(buffer).find_last_of("\\/");
    return string(buffer).substr(0, pos);
}

tuple<string, string, int> read_config(const string &config_file) {
    ifstream file(config_file);
    if (!file) {
        cerr << "Unable to open config file" << endl;
        exit(1);
    }

    string folder_path, color_code;
    int scroll_speed;
    string line;
    int config_counter = 0;
    while (getline(file, line)) {
        // Ignore comment lines starting with '#'
        if (line.empty() || line[0] == '#') {
            continue;
        }
        if (config_counter == 0) {
            folder_path = line;
        } else if (config_counter == 1) {
            color_code = line;
        } else {
            scroll_speed = stoi(line);
            break;
        }
        config_counter++;
    }

    file.close();

    return {folder_path, color_code, scroll_speed};
}

int main() {
    string config_file = get_executable_path() + "\\asciidle.cf";
    auto config_values = read_config(config_file);
    string ascii_art_folder = get<0>(config_values);
    string color_code = get<1>(config_values);
    int scroll_speed = get<2>(config_values);
    if (ascii_art_folder.empty()) {
        cerr << "Invalid folder path in config file, exiting..." << endl;
        return 1;
    }
    string ascii_art_file;

    srand(time(NULL));

    // Set the console mode to enable virtual terminal sequences
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD dwMode = 0;
    GetConsoleMode(hOut, &dwMode);
    dwMode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING;
    SetConsoleMode(hOut, dwMode);

    int row = 0;
    while (1) {
        random_ascii_art(ascii_art_folder, ascii_art_file);
        display_ascii_art(ascii_art_file, row, color_code, scroll_speed);
        this_thread::sleep_for(chrono::milliseconds(2));
    }

    return 0;
}

void display_ascii_art(const string &filename, int &row, const string &color_code, int scroll_speed) {
    ifstream file(filename);
    if (!file) {
        cerr << "Unable to open ASCII art file" << endl;
        exit(1);
    }

    int console_width = get_console_width();
    string line;
    while (getline(file, line)) {
        string truncated_line = line.substr(0, console_width);
        cout << "\033[" << row << ";0H\033[" << color_code << "m" << truncated_line << "\033[0m" << endl;
        row++;
        this_thread::sleep_for(chrono::milliseconds(scroll_speed));
    }

    file.close();
}

bool has_txt_extension(const string &filename) {
    size_t dot_pos = filename.find_last_of('.');
    return (dot_pos != string::npos && filename.substr(dot_pos) == ".txt");
}

void random_ascii_art(const string &folder, string &filename) {
    vector<string> files;
    WIN32_FIND_DATA fd;
    HANDLE hFind = FindFirstFile((folder + "\\*.txt").c_str(), &fd);
    if (hFind != INVALID_HANDLE_VALUE) {
        do {
            if (!(fd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
                files.emplace_back(fd.cFileName);
            }
        } while (FindNextFile(hFind, &fd));
        FindClose(hFind);
    } else {
        cerr << "Unable to open directory" << endl;
        exit(1);
    }

    if (files.empty()) {
        cerr << "No ASCII art files found" << endl;
        exit(1);
    }

    int random_file = rand() % files.size();
    filename = folder + "\\" + files[random_file];
}

int get_console_width() {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
    return csbi.srWindow.Right - csbi.srWindow.Left + 1;
}

