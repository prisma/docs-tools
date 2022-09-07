export interface FilePath {
    [key: string]: string | undefined;
    current_path: string;
    new_path: string;
    name?: string;
}