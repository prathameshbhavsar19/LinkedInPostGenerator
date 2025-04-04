import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def process_posts(raw_file_path, processed_file_path = "data/processeed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['caption'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for epost in enriched_posts:
        current_tags = epost['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)

def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list = ', '.join(unique_tags)
    template = '''
        You will be given a list of social media post captions along with their engagement numbers.

        Your task is to analyze and unify tags/themes that emerge from the post content.

        Follow these guidelines:

        1. Identify keywords, topics, or themes (e.g., "AI Agents", "GPT-4o", "Zapier", "Data Intelligence").
        2. Group related tags under a single, clean, generalized tag.
        Example 1: "GPT-4o", "DeepSeek", "Claude" → "LLM Models"
        Example 2: "Zapier", "Integration", "Automation" → "AI Tools"
        Example 3: "GTC 2025", "Jensen Huang", "NVIDIA" → "AI Events"
        Example 4: "Career Advice", "Personal Growth", "Authenticity" → "Mindset"

        3. Ensure tags use Title Case (e.g., "AI Tools", "Productivity", "LLM Models")
        4. Output a JSON object where:
        - keys are the original tags or keywords
        - values are the unified tag/category
        5. Keep the output clean — no extra commentary or explanation.
        
        Here is a list of tags:
        {tags}
        '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'tags': str(unique_tags_list)})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)

    except OutputParserException:
        raise OutputParserException("Content too Big. Unable to parse jobs.")


    return res 
    

def extract_metadata(post):
    template = '''
    You are given a LinkedIn Post. You need to extract number of lines, Topic of the post based on the caption and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object shpuld have exactly hree keys: line_count, topic and tags.
    3. tags is an array of text tags. Extract maximum two tags, don't return something blank give atleast two tags
    4. Topic should be one liner, something which summarizes the entire caption.

    Here is the actual post on which you need to perform this task:
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post' : post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)

    except OutputParserException:
        raise OutputParserException("Content too Big. Unable to parse jobs.")


    return res


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")