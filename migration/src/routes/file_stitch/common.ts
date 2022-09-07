export interface BodyPart {
    index: number;
    key: string;
}
export interface FilePath { 
    new_path: string;
    name?: string;
    headers: string[];
    body: BodyPart[];
};