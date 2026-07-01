import requests

hf_api_key = ""
model_id = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{model_id}"
headers = {"Authorization": f"Bearer {hf_api_key}"}
topics = ['politics', 'technology', "sports", 'health', "business"]

def ask_hf(headline: str):
    payload= { input: headline, "parameters": {"candidate_labels": topics}}

    r= requests.post(API_URL, HEADERS=headers, json=payload,timeout=30)

    if not r.ok:
        raise RuntimeError(f"H_F error {r.status_code}: {r.text}")
    return r.json()

def best_topic(preds: list):
    best = max(preds, key=lambda x: x['score'])
    return best['label'], best['score']

def bar(score: float):
    pct = score * 100
    block= int(pct // 10)
    return "█"*block + "░"*(10-block)

def show(headline: str, preds: list):
    top_lebel, top_score = best_topic(preds)
    print('\n'+'='*60)
    print("??? news classifier")
    print('='*60)
    print(f"Headline: {headline}")
    print(f'best topic: {top_lebel} ')
    print(f'confidence:{round(top_score*100,1)}%[{bar(top_score)}]')

    print('\n top 3 guesses:')
    top_3 = sorted(preds, key=lambda x: x['score'], reverse=True)[:3]
    for i,p in enumerate(top_3, start=1):
        print(f"{i}. {p['label']:<11} {round(p['score']*100,1)}% [{bar(p['score'])}]")
    print('='*60)