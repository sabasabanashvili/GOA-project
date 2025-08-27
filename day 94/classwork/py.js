class FunctionalSet {
    constructor(elementsOrFunc, eqFunc) {
        if (typeof elementsOrFunc === 'function') {
            this._isFunc = true;
            this._membership = elementsOrFunc;
            this._eq = null;
            this._elements = null;
        } else {
            this._isFunc = false;
            this._elements = [];
            this._eq = eqFunc || ((a, b) => a === b);
            if (Array.isArray(elementsOrFunc)) {
                for (const el of elementsOrFunc) {
                    if (!this._elements.some(e => this._eq(e, el))) {
                        this._elements.push(el);
                    }
                }
            }
            this._membership = null;
        }
    }

    _throwIfFunc(method) {
        if (this._isFunc) throw new TypeError(`Cannot call ${method} on functional set`);
    }

    has(x) {
        if (this._isFunc) return !!this._membership(x);
        return this._elements.some(e => this._eq(e, x));
    }

    union(other) {
        if (this._isFunc || other._isFunc) {
            const f1 = this._isFunc ? this._membership : x => this.has(x);
            const f2 = other._isFunc ? other._membership : x => other.has(x);
            return new FunctionalSet(x => f1(x) || f2(x));
        }
        const eq = this._eq;
        const newEls = this._elements.slice();
        for (const el of other._elements) {
            if (!newEls.some(e => eq(e, el))) newEls.push(el);
        }
        return new FunctionalSet(newEls, eq);
    }

    intersection(other) {
        if (this._isFunc || other._isFunc) {
            const f1 = this._isFunc ? this._membership : x => this.has(x);
            const f2 = other._isFunc ? other._membership : x => other.has(x);
            return new FunctionalSet(x => f1(x) && f2(x));
        }
        const eq = this._eq;
        const newEls = this._elements.filter(e => other._elements.some(o => eq(e, o)));
        return new FunctionalSet(newEls, eq);
    }

    difference(other) {
        if (this._isFunc || other._isFunc) {
            const f1 = this._isFunc ? this._membership : x => this.has(x);
            const f2 = other._isFunc ? other._membership : x => other.has(x);
            return new FunctionalSet(x => f1(x) && !f2(x));
        }
        const eq = this._eq;
        const newEls = this._elements.filter(e => !other._elements.some(o => eq(e, o)));
        return new FunctionalSet(newEls, eq);
    }

    not() {
        if (this._isFunc) {
            return new FunctionalSet(x => !this._membership(x));
        }
        const eq = this._eq;
        return new FunctionalSet(x => !this._elements.some(e => eq(e, x)));
    }

    isEmpty() {
        this._throwIfFunc('isEmpty');
        return this._elements.length === 0;
    }

    isUniversal() {
        this._throwIfFunc('isUniversal');
        // Only possible if set is complement of empty set
        // But since we can't know the universe, we define universal as complement of empty set
        return false;
    }

    includes(other) {
        this._throwIfFunc('includes');
        if (other._isFunc) throw new TypeError('Cannot call includes with functional set');
        return other._elements.every(e => this._elements.some(me => this._eq(me, e)));
    }

    equals(other) {
        this._throwIfFunc('equals');
        if (other._isFunc) throw new TypeError('Cannot call equals with functional set');
        if (this._elements.length !== other._elements.length) return false;
        return this.includes(other) && other.includes(this);
    }
}

module.exports = FunctionalSet;