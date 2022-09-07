export interface BodyPart {
    index: number;
    key: string;
}
export interface FilePath { 
    new_path: string;
    name?: string;
    header: string[];
    body: BodyPart[];
};